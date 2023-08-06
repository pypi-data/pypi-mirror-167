# -*- coding:utf-8 -*-
import json
import datetime
import sys
import logging
import os
from .apolloInterface import ApolloUpdateItems


def getLog():
    logger = logging.getLogger()  # 创建一个logger
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()  # 创建一个handler，用于输出到控制台
    ch.setLevel(logging.INFO)
    # 定义handler的输出格式
    formatter = logging.Formatter(fmt="%(asctime)s-[%(levelname)s] :  %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


def backup_config(config_msg, version_cache_dir='/tmp/backUpApolloVersion', app="", namespace=''):
    try:
        if not os.path.exists(version_cache_dir):
            os.makedirs(version_cache_dir)
        if not isinstance(config_msg, str):
            config_msg = json.dumps(config_msg, ensure_ascii=False)
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = "{}_{}_{}.json".format(app, namespace, now)
        cache_file = os.path.join(version_cache_dir, filename)

        with open(cache_file, 'w') as fw:
            fw.write(config_msg)
            fw.close()
        logger.info("[备份]:版本数据备份完成，数据写入{}文件完成".format(cache_file))
    except Exception as e:
        logger.error("[备份]:版本文件备份失败，出现异常：{}".format(e))


ExitCode = 0
OLD_VERSIONS = {}
logger = getLog()


class ApolloUpdate(ApolloUpdateItems):

    def __init__(self, addr, name, password):
        """
        :param addr:apollo地址信息
        :param name: 用户名
        :param password: 用户密码
        :return
        """
        super().__init__(addr, name, password)

    def run_action(self, action, key="", value="", **kwargs):
        """
        apollo 配置执行操作
        :param action: 执行操作CRUD
        :param key: 执行操作的字段app.namespaces.key值
        :param value: 执行操作的字段app.namespaces.value值，action为delete时可不提供
        :return:
        """
        first_release_dict = self.get_releases_msg(0, 2)[1]  # 查询最新的版本基线信息
        first_release_name = first_release_dict.get("name", "")
        first_release_id = first_release_dict.get("id", "")
        logger.info("修改前的版本基线信息，name:{},ID:{}".format(first_release_name, first_release_id))

        if action == 'create':  # 创建配置字段
            run_flag, run_result = self.create_msg(key, value)
        elif action == 'update':  # 修改配置字段值
            run_flag, run_result = self.update_msg(key, value)
        elif action == 'search':  # 查询app.namespaces.items下的值
            run_flag, run_result = self.search_msg()
        elif action == 'delete':  # 单个字段的删除
            run_flag, run_result = self.delete_msg(key)
        else:
            run_flag, run_result = False, "动作参数输入错误"
        logger.info("{}执行{},运行Result:{},Message:{}".format("=" * 10, action, run_flag, run_result))

        if run_flag:
            # 数据变更后的版本发布
            # 执行一次操作，需要发布一次，因为批量传入的数据不能保证是同一个app.namespaces下，所以一次crud发布一次版本
            release_flag, release_title = self.release_msg()
            logger.info("{}执行发布，运行Result:{},基线版本号：{}".format("=" * 10, release_flag, release_title))
        else:
            logger.warning("=" * 10 + "当前操作不支持执行发布")

        last_release_dict = self.get_releases_msg(0, 2)[1]  # 查询最新的版本基线信息
        last_release_name = last_release_dict.get("name", "")
        last_release_id = last_release_dict.get("id", "")
        logger.info("修改后的版本基线信息，name:{},ID:{}".format(last_release_name, last_release_id))

        change_msg = self.compare_release_msg(first_release_id, last_release_id)  # 查询打印变更数据
        changes_list = change_msg.get("changes", [])
        changes_str_list = list(map(str, changes_list))
        logger.info("{}当前操作变更字段{}个，变更数据为{}".format("=" * 10, len(changes_str_list), ''.join(changes_str_list)))

        vertify_result = False
        if changes_list:  # 变更数据验证
            key_cg = changes_list[0].get("entity", {}).get("secondEntity", {}).get("key", '')  # 变更的字段名
            value_cg = changes_list[0].get("entity", {}).get("secondEntity", {}).get("value", '')  # 变更的字段值
            if action in ["create", "update"] and key == key_cg and value == value_cg:
                vertify_result = True
            elif action == 'delete' and key_cg == key and value_cg == '':
                vertify_result = True
            else:
                vertify_result = False
        elif action == "create" and run_flag and not first_release_id:
            vertify_result = True
            logger.warning("无法查询到上一个发布版本信息，当前新增数据{}".format(last_release_dict.get('configurations', {})))
        logger.info("数据验证结果：{} \n".format(vertify_result))
        return vertify_result, last_release_name

    def main_CRUD2(self, items_data, version_cache_dir="/tmp/backUpApolloVersion"):
        """
        数据增删改查
        :step1 解析入参items_data
        :step2 将同样的命名空间的数据放到同一个字典之中dic_data={app.namespace: {items: [], # 所有要修改的数据
                                                                        firstversion: {}, # 修改前当前空间下的最新版本数据
                                                                        lastVersion: {},# 修改后的当前空间下的最新版本数据
                                                                        flag:""# 变更状况，如果有数据变更失败，不执行发布
                                                                        }...}
        :step3 修改字典里面的初始版本数据，注意无初始版本的状况
        :step4 解析字典，对item里面数据实现变更,记录执行结果数据flag
        :step5 解析遍历dic_data，实现版本发布，对flag为False的app.namespace下的数据不执行发布；然后获取app.namespace最新的版本
               数据，进行数据验证,记录数据验证状况
        :step6 整体执行状况进行判断，如果有版本未发布、或者数据校验错误，整体执行失败，上报告警

        :param items_data:
        :return:
        """
        result_json = {}
        result_fflag = True
        global OLD_VERSIONS, ExitCode

        if not items_data:
            logger.error("=============================变更数据异常，检测传入数据列表===================================")
            ExitCode = -1
            sys.exit(-1)
        all_data = {}
        for items in items_data:  # 解析数据，按命名空间归类数据，查询各个空间的最新版本数据
            apps = items.get("apps")
            namespace = items.get("namespaces")
            env = items.get("env")
            cluster = items.get("clusters")
            tempKey = "{}.{}".format(apps, namespace)
            if all_data.get(tempKey, {}):
                all_data[tempKey]["items"].append(items)
            else:
                all_data[tempKey] = {
                    "items": [items],  # 所有要修改的数据
                    "apps": apps,
                    "namespaces": namespace,
                    "clusters": cluster,
                    "env": env,
                    "first_release_id": '',  # 修改前当前空间下的最新版本数据
                    "flag": "",  # 变更状况，如果有数据变更失败，不执行发布
                }

        for dt_json in all_data.values():
            apps = dt_json.get("apps")
            namespace = dt_json.get("namespaces")
            env = dt_json.get("env")
            cluster = dt_json.get("clusters")
            items = dt_json.get("items")
            tempKey = "{}.{}".format(apps, namespace)
            logger.info("{fmt}{msg}{fmt}".format(fmt="=" * 25,
                                                 msg="app.namespace【{}.{}】配置执行变更".format(apps, namespace)))
            self.set_apollo_cfg(app=apps, namespaces=namespace, clusters=cluster, env=env)
            first_release_dict = self.get_releases_msg(0, 2)[1]  # 查询最新的版本基线信息
            first_release_name = first_release_dict.get("name", "")
            first_release_id = first_release_dict.get("id", "")
            logger.info("[版本查询]:命名空间【{}.{}】配置变更前版本查询，最新版本为：{}".format(apps, namespace, first_release_name))
            OLD_VERSIONS["{app}.{namespaces}".format(app=apps, namespaces=namespace)] = first_release_name
            backup_config(first_release_dict, version_cache_dir=version_cache_dir,
                          app=apps, namespace=namespace)  # 最新配置备份
            flag_crud = True
            kv_input = {}
            for item in list(items):
                key = item.get("key")
                value = item.get("value")  #
                action = item.get("action")
                kv_input[key] = value
                if action == 'create':  # 创建配置字段
                    run_flag, run_result = self.create_msg(key, value)
                elif action == 'update':  # 修改配置字段值
                    run_flag, run_result = self.update_msg(key, value)
                elif action == 'delete':  # 单个字段的删除
                    run_flag, run_result = self.delete_msg(key)
                else:
                    run_flag, run_result = False, "动作参数输入错误"
                if not run_flag:
                    flag_crud = False  # 如果有一条数据执行出错，改空间下整体数据标记异常
                    logger.error("[配置修改]:执行{},运行Result:{},Message:{}".format(action, run_flag, run_result))
                else:
                    logger.info("[配置修改]:执行{},运行Result:{},Message:{}".format(action, run_flag, run_result))
            dt_json["flag"] = flag_crud  # todo 此处开始往下，代码可以注释
            dt_json["kv_input"] = kv_input
            dt_json["first_release_id"] = first_release_id
            all_data[tempKey] = dt_json
            logger.info("{fmt}".format(fmt="-" * 80))

        for dt_json in all_data.values():
            apps = dt_json.get("apps")
            namespace = dt_json.get("namespaces")
            env = dt_json.get("env")
            cluster = dt_json.get("clusters")
            items = dt_json.get("items")
            flag_crud = dt_json["flag"]
            kv_input = dt_json["kv_input"]
            first_release_id = dt_json["first_release_id"]
            tempKey = "{}.{}".format(apps, namespace)  # todo 此处结束，此区间内的代码注释后不影响功能运行，影响日志显示样式
            logger.info("{fmt}{msg}{fmt}".format(fmt="=" * 20,
                                                 msg="app.namespace【{}.{}】版本发布及数据校验".format(apps, namespace)))
            self.set_apollo_cfg(app=apps, namespaces=namespace, clusters=cluster, env=env)
            if flag_crud:
                # 数据变更后的版本发布
                # 执行一次操作，需要发布一次，因为批量传入的数据不能保证是同一个app.namespaces下，所以一次crud发布一次版本
                release_flag, release_title = self.release_msg()
                logger.info("[版本发布]:执行发布，运行Result:{},基线版本号：{}".format(release_flag, release_title))
            else:
                logger.error("[版本发布]:当前空间下数据变更异常，不支持执行发布")
                result_fflag = False
                result_json[tempKey] = "当前未发布新版本"
                continue

            last_release_dict = self.get_releases_msg(0, 2)[1]  # 查询最新的版本基线信息
            last_release_name = last_release_dict.get("name", "")
            last_release_id = last_release_dict.get("id", "")
            last_release_cfg = last_release_dict.get('configurations', {})
            last_release_cfg = last_release_cfg if isinstance(last_release_cfg, dict) else eval(last_release_cfg)
            logger.info("[版本查询]:命名空间【{}.{}】配置变更后版本查询，最新版本为：{}".format(apps, namespace, last_release_name))

            change_msg = self.compare_release_msg(first_release_id, last_release_id)  # 查询打印变更数据
            change_data = {}
            changes_list = change_msg.get("changes", [])
            if first_release_id and changes_list:
                for change_dt in changes_list:
                    firstEntity = change_dt.get("entity", {}).get('firstEntity', {})
                    secondEntity = change_dt.get("entity", {}).get('secondEntity', {})
                    k = firstEntity.get("key") if firstEntity.get("key", '') else secondEntity.get("key")
                    v = firstEntity.get("value") if firstEntity.get("value", '') else secondEntity.get("value")
                    change_data[k] = v
            elif first_release_id and not changes_list:
                pass
            else:
                change_data = kv_input

            different1 = set(kv_input.keys()).difference(set(change_data.keys()))  # 差集 输入有此字段，比对结果无改字段’
            different2 = list(
                set(kv_input.keys()).symmetric_difference(set(change_data.keys())))  # 有对称差集（项在a或b中，但不会同时出现在二者中）
            if different1 and different1 < set(last_release_cfg.keys()):
                # 此处校验针对update，update时，a1原始值为1，要修改为1，此时输入数据集与修改后比对数据结果集会出现数据偏差
                logger.info("[数据验证]:输入数据与变更后的数据一致")
                result_json[tempKey] = last_release_name
            elif different2 and not (different1 and different1 < set(last_release_cfg.keys())):
                # 比对输入参数与变更数据是否一致
                logger.error("[数据验证]:命名空间下入参数据与变更的数据内容存在差异")
                logger.info("[数据验证]：入参数据{}".format(kv_input))
                logger.info("[数据验证]：变更后的数据{}".format(change_data))
                result_fflag = False
                result_json[tempKey] = last_release_name
            # elif len(items) != len(change_data):
            #    # 此处验证输入数据个数和被修改的数据个数是否一致
            #     result_json[tempKey] = ''
            #     logger.error("[数据验证]:命名空间下入参数据与变更的数据数量存在差异")
            #     logger.info("[数据验证]：入参数据{}".format(kv_input))
            #     logger.info("[数据验证]：变更后的数据{}".format(change_data))
            #     result_fflag = False
            #     result_json[tempKey] = last_release_name
            else:
                logger.info("[数据验证]:输入数据与变更后的数据一致")
                result_json[tempKey] = last_release_name

        return result_fflag, result_json

        # todo 记录执行状况

    def main_CRUD(self, items_data):
        """
        数据增删改查
        :param items_data:
        :return:
        """
        global ExitCode
        result_vertify = True
        release_version_list = []
        if not items_data:
            logger.error("=============================变更数据异常，检测传入数据列表===================================")
            ExitCode = -1
            sys.exit(-1)
        for items in items_data:
            action = items.get("action")
            item_key = items.get("key")
            item_value = items.get("value")
            apps = items.get("apps")
            namespace = items.get("namespaces")
            env = items.get("env")
            cluster = items.get("clusters")
            self.set_apollo_cfg(app=apps, namespaces=namespace, clusters=cluster, env=env)
            run_reault, release_title = self.run_action(action, key=item_key, value=item_value)
            release_version_list.append(release_title)
            if not run_reault:
                result_vertify = False
        if not result_vertify:
            logger.error("执行结果中存在执行失败或执行前后无数据改变的状况存在，请排查日志")
            ExitCode = -1
            sys.exit(-1)
        else:
            logger.info("所有数据已变更完成,配置修改成功")
        return release_version_list[0]

    def update_data_2_roll_release(self, release_title, last_release_data):
        """
        使用增删改查修改版本数据，然后使用目标版本发布，实现回滚的目的
        :param release_title: 要回滚的目标版本号
        :param last_release_data: 当前版本的配置数据信息
        :return:
        """
        global ExitCode
        result_flag = True
        release_flag, release_dicts = self.get_releases_msg(get_all=True)  # 获取所有发布版本信息
        goal_dict = {}
        for release_dict in release_dicts:
            release_name = release_dict.get("name", "")
            if release_name == release_title:
                goal_dict = release_dict
                try:
                    self.rollback_release(release_dict)
                except Exception as e:
                    logger.error(e)
        if not goal_dict:
            logger.error("回滚版本id数据获取失败，取消数据回滚")
            ExitCode = -1
            sys.exit(-1)
        else:
            logger.info("[Data]:需要回滚到的版本基线信息，name:{} ,Data:{}\n\t".format(release_title, goal_dict))

        # fun 1 ：对比release_dict和last_release_data数据，执行增删改查 发布使用要回滚的版本号
        logger.info("{fs}版本号回滚完成，开始修改配置{fs}".format(fs="=" * 20))
        curren_cfg = last_release_data.get('configurations', {})
        goal_cfg = goal_dict.get('configurations', {})
        curren_cfg = curren_cfg if isinstance(curren_cfg, dict) else eval(curren_cfg)  # 无语，奇葩，怎么前面json转化过了，还要再转化
        goal_cfg = goal_cfg if isinstance(goal_cfg, dict) else eval(goal_cfg)
        curren_cfg_keys = list(curren_cfg.keys())  # 当前版本字段
        goal_cfg_keys = list(goal_cfg.keys())  # 目标版本字段
        others = list(set(goal_cfg_keys).difference(set(curren_cfg_keys)))  # 目标版本存在、当前版本不存在的字段
        logger.info("[Data]:当前版本的字段信息：{}".format(curren_cfg_keys))
        logger.info("[Data]:需要回滚版本的字段信息：{}".format(goal_cfg_keys))

        for key in curren_cfg_keys + others:
            if key in goal_cfg_keys and key in curren_cfg_keys:  # 两个版本都存在的字段
                value = goal_cfg.get(key, "")
                run_flag, run_result = self.update_msg(key, value)  # 修改字段
                logger.info("修改字段{}的为{}".format(key, value))
            elif key in goal_cfg_keys and key not in curren_cfg_keys:  # 当前版本不存在、目标版本存在的字段
                value = goal_cfg.get(key, "")
                run_flag, run_result = self.create_msg(key, value)  # 创建配置字段
                logger.info("新增字段{}的为{}".format(key, value))
            else:  # 当前版本存在、目标版本不存在的字段
                run_flag, run_result = self.delete_msg(key)
                logger.info("删除字段{}".format(key))

            if not run_flag:
                result_flag = False

        release_flag, release_title = self.release_msg(release_title)
        logger.info("[版本发布]:执行发布，运行Result:{},基线版本号：{}".format(release_flag, release_title))
        if not release_flag:
            result_flag = False
        return result_flag, release_title

    def main_rollback(self, release_version, apps, namespace, env="PRO", cluster="default"):
        """
        数据回滚
        :param release_version: 版本号
        :param apps: app名称
        :param namespace: 命名空间
        :param env: 环境名称
        :param cluster: 集群名称
        :return:
        """
        global OLD_VERSIONS, ExitCode
        self.set_apollo_cfg(app=apps, namespaces=namespace, clusters=cluster, env=env)  # 设置操作维度空间
        if (not release_version) or (not apps) or (not namespace):
            logger.error("=============================回滚异常，检测传入数据列表===================================")
            logger.error("apps:{},namespaces:{},release_version:{}".format(apps, namespace, release_version))
            ExitCode = -1
            sys.exit(-1)

        current_release_dict = self.get_releases_msg(0, 2)[1]  # 查询最新的版本基线信息
        first_release_name = current_release_dict.get("name", "")
        first_release_id = current_release_dict.get("id", "")
        logger.info("[版本查询]:命名空间【{}.{}】配置变更前版本查询，最新版本为：{}".format(apps, namespace, first_release_name))
        OLD_VERSIONS["{app}.{namespaces}".format(app=apps, namespaces=namespace)] = first_release_name
        if first_release_name == release_version:
            logger.error("需要回滚的版本与当前正在使用的版本号相同，取消版本回滚")
            ExitCode = -1
            sys.exit(-1)

        logger.info("{fmt}{msg}{fmt}".format(fmt="=" * 30, msg="命名空间【{}.{}】执行版本回滚".format(apps, namespace)))
        run_flag, run_result = self.update_data_2_roll_release(release_version, current_release_dict)  # 执行版本回滚
        logger.info("[Result]:执行rollback结束,运行Result:{},Message:{}".format(run_flag, run_result))

        last_release_dict = self.get_releases_msg(0, 2)[1]  # 查询最新的版本基线信息
        last_release_name = last_release_dict.get("name", "")
        last_release_id = last_release_dict.get("id", "")
        logger.info("[版本查询]:命名空间【{}.{}】配置变更后版本查询，最新版本为：{}".format(apps, namespace, first_release_name))

        change_msg = self.compare_release_msg(first_release_id, last_release_id)  # 查询打印变更数据
        changes_list = change_msg.get("changes", [])
        changes_str_list = list(map(str, changes_list))
        logger.info(
            "[变更数据]：{}当前操作变更字段{}个，变更数据为{} \n".format("=" * 10, len(changes_str_list), ''.join(changes_str_list)))

        if last_release_name != release_version:
            logger.error("[执行结果]：回滚执行异常，请排查日志")
            ExitCode = -1
            sys.exit(-1)
        else:
            logger.info("[执行结果]：所有数据已回滚完成,执行成功")
        return last_release_name
