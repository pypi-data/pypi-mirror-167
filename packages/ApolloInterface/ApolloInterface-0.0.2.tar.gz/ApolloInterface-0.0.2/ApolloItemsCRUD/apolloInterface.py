# -*- coding:utf-8 -*-
# author:hts
# email:2081981735@qq.com
import requests
import json
import datetime
import sys


class ApolloUpdateItems():

    def __init__(self, addr, name, password):
        """
        :param addr:apollo地址信息
        :param name: 用户名
        :param password: 用户密码
        :return
        """
        self.addr = addr
        self.name = name
        self.password = password
        self.header = {
            'content-type': "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }
        self.session = None
        self.login()

    def set_apollo_cfg(self, app='', namespaces='', clusters='default', env="PRO"):
        """
        Apollo支持4个维度管理Key-Value格式的配置,环境设置,变更操作维度
        :param app: app应用名称
        :param namespaces:命名空间
        :param clusters:集群名称
        :param env:环境信息
        :return:
        """
        self.app = app
        self.namespaces = namespaces
        self.clusters = clusters
        self.env = env

    def login(self):
        try:
            url_login = 'http://{}/signin?'.format(self.addr)
            self.session = requests.Session()
            self.session.get(url_login, auth=(self.name, self.password), verify=False)  # 登录
            print("apollo登录成功")
        except Exception as e:
            print("登录失败，请排查登录信息是否输入正确")
            sys.exit()

    def create_msg(self, key, value):
        """
        app.namespaces下创建key-value字段值
        :param key: 字段名称
        :param value: 字段值
        :return: 执行结果
        """
        url_create = "http://{addr}/apps/{apps}/envs/{env}/clusters/{clusters}/namespaces/{namespaces}/item".format(
            addr=self.addr,
            env=self.env,
            apps=self.app,
            clusters=self.clusters,
            namespaces=self.namespaces
        )
        body = {
            "tableViewOperType": "create",
            "key": key,
            "value": value,
            "addItemBtnDisabled": True
        }
        response = self.session.post(url_create, data=json.dumps(body), headers=self.header)
        code, text = response.status_code, response.text
        result_flag = True if code == 200 else False
        if result_flag:
            result_msg = '{}.{}.{}字段创建成功,执行结果code:{}'.format(self.app, self.namespaces, key, code)
        else:
            print("数据创建请求执行错误,text:{}".format(text))
            result_msg = '{}.{}.{}字段创建失败,执行结果code:{}'.format(self.app, self.namespaces, key, code)
        return result_flag, result_msg

    def update_msg(self, key, value):
        """
        app.namespaces下查找key字段信息，更新字段字典的value值
        :param key: 查找和更新的item key
        :param value: 更新的value值
        :return: 执行结果信息
        """
        result_flag, result_update = False, ''
        url_update = "http://{addr}/apps/{apps}/envs/{env}/clusters/{clusters}/namespaces/{namespaces}/item".format(
            addr=self.addr,
            env=self.env,
            apps=self.app,
            clusters=self.clusters,
            namespaces=self.namespaces)

        flag_search, json_data = self.search_msg()  # 查询当前app.namespaces下的字段信息
        if flag_search and json_data:
            for json_d in json_data:
                jd_key = json_d.get("key", "")
                if jd_key != key:
                    continue
                json_d["tableViewOperType"] = "update"
                json_d['value'] = value  # 匹配到字段，更新数据
                response = self.session.put(url_update, data=json.dumps(json_d), headers=self.header)
                code, text = response.status_code, response.text
                result_flag = True if code == 200 else False
                if not result_flag:
                    print("数据更新请求执行错误,text:{}".format(text))
                result_update = '匹配到字段{}.{}.{}信息,更新结束，执行结果code:{}'.format(self.app,
                                                                          self.namespaces,
                                                                          key, code)
                break
            else:
                result_update = '查询结果无法匹配到字段{}.{}.{}信息,请人工排查数据准确性，更新结束'.format(self.app,
                                                                               self.namespaces, key)
        else:
            result_update = '数据更新失败,未查询到namespaces下字段信息或{}.{}信息查询失败或，请人工排查确认'.format(self.app,
                                                                                     self.namespaces)
        return result_flag, result_update

    def delete_msg(self, key, value=''):
        """
        app.namespaces下删除字段信息
        :param key: 需要删除的key
        :param value: 需要删除的value，此处未使用
        :return: 执行结果信息
        """
        result_flag, result_delete = False, ''
        url_del = "http://{addr}/apps/{apps}/envs/{env}/clusters/{clusters}/namespaces/{namespaces}/items/{i_d}"
        flag_search, json_data = self.search_msg()  # 查询当前app.namespaces下的字段信息
        if flag_search and json_data:
            for json_d in json_data:
                jd_key = json_d.get("key", "")
                key_id = json_d.get("id")
                if jd_key != key:
                    continue
                url_del = url_del.format(addr=self.addr,
                                         apps=self.app,
                                         env=self.env,
                                         clusters=self.clusters,
                                         namespaces=self.namespaces,
                                         i_d=key_id)
                response = self.session.delete(url_del, headers=self.header)
                code, text = response.status_code, response.text
                result_flag = True if code == 200 else False
                if not result_flag:
                    print("数据删除请求执行错误,text:{}".format(text))
                result_delete = '匹配到字段{}.{}.{}信息,删除结束，执行结果code:{}'.format(self.app,
                                                                          self.namespaces,
                                                                          key, code)
                break
            else:
                result_delete = '查询结果无法匹配到字段{}.{}.{}信息,请人工排查数据准确性，删除结束'.format(self.app,
                                                                               self.namespaces, key)
        else:
            result_delete = '数据删除失败,未查询到namespaces下字段信息或{}.{}信息查询失败或，请人工排查确认'.format(self.app, self.namespaces)
        return result_flag, result_delete

    def search_msg(self, ifText=False, ifEval=False):
        """
        查询app.namespaces字段信息
        :return:
        """
        url_search = "http://{addr}/apps/{apps}/envs/{env}/clusters/{clusters}/namespaces/{namespaces}/items".format(
            addr=self.addr,
            apps=self.app,
            env=self.env,
            clusters=self.clusters,
            namespaces=self.namespaces
        )
        response = self.session.get(url_search, headers=self.header)
        json_data = response.json()
        text = response.text
        flag = True if response.status_code == 200 else False
        if ifEval:
            return flag, eval(text)
        elif ifText:
            return flag, text
        else:
            return flag, json_data

    def release_msg(self, releaseTitle=""):
        """
        版本发布
        :return:
        """
        url_release = "http://{addr}/apps/{apps}/envs/{env}/clusters/{clusters}/namespaces/{namespaces}/releases".format(
            addr=self.addr,
            apps=self.app,
            env=self.env,
            clusters=self.clusters,
            namespaces=self.namespaces)
        if not releaseTitle:
            releaseTitle = datetime.datetime.now().strftime("%Y%m%d%H%M%S_release_by_automation")
        release_data = {
            "releaseTitle": releaseTitle,
            "releaseComment": "",
            "isEmergencyPublish": False
        }
        response = self.session.post(url_release, data=json.dumps(release_data), headers=self.header)
        flag = True if response.status_code == 200 else False
        return flag, releaseTitle

    def get_releases_msg(self, page=0, size=10000, release_title='', get_all=False):
        """
        查询发布版本信息
        :param page: 查询分页页码
        :param size: 查询分页页面数据量
        :param release_title: 发布版本名称，有值执行匹配，物质返回最新的发布版本id数据信息
        :return:
        """
        url = ("http://{addr}/apps/{apps}/envs/{env}/clusters/{clusters}/namespaces/{namespaces}/releases/active?"
               "page={page}&size={size}".format(addr=self.addr,
                                                apps=self.app,
                                                env=self.env,
                                                clusters=self.clusters,
                                                namespaces=self.namespaces,
                                                page=page,
                                                size=size))
        response = self.session.get(url, headers=self.header)
        json_data = response.json()
        result_flag, result_dict = False, {}
        if response.status_code != 200:  # 数据查询请求执行失败
            print("数据删除请求执行错误,code:{}".format(response.status_code), response.text)
        else:
            if release_title:  # 有发布版本名称传入，返回匹配到的数据
                for json_d in json_data:
                    name = json_d.get("name", '')
                    if name == release_title:
                        result_flag, result_dict = True, json_d
                        break
            elif get_all:
                result_flag, result_dict = True, json_data
            else:
                result_flag, result_dict = True, json_data[0] if json_data else {}
        return result_flag, result_dict

    def compare_release_msg(self, first_release_id, last_release_id):
        """
        比较发布前后数据变更详情
        :param first_release_id: 上一个发布版本的id信息
        :param last_release_id: 后一个发布版本的id信息
        :return:
        """
        url = ('http://{addr}/envs/{env}/releases/compare?baseReleaseId={first_release_id}&'
               'toCompareReleaseId={last_release_id}'.format(addr=self.addr,
                                                             apps=self.app,
                                                             env=self.env,
                                                             first_release_id=first_release_id,
                                                             last_release_id=last_release_id))
        response = self.session.get(url, headers=self.header)
        json_data = response.json()
        code, text = response.status_code, response.text
        result_flag = True if code == 200 else False
        if not result_flag:
            print("数据比对请求执行错误.{}".format(text))
        return json_data

    def rollback_release(self, release_dict):
        """
        接口实现发布的版本回滚
        :param kwargs:
        :return:
        """
        # release_flag, release_dict = self.get_releases_msg(release_title=release_title)
        release_id = release_dict.get("id", "")
        release_title = release_dict.get("name", "")
        if not release_id:
            print("回滚版本id数据获取失败，取消数据回滚")
            sys.exit(-1)

        url = "http://{addr}/envs/{env}/releases/{release_id}/rollback".format(addr=self.addr, env=self.env,
                                                                               release_id=release_id)
        print("开始回滚版本name:{},id:{},url:{}".format(release_title, release_id, url))
        response = self.session.put(url, headers=self.header)
        if response.status_code != 200:  # 数据查询请求执行失败
            print("数据删除请求执行错误,code:{},text:{}".format(response.status_code, response.text))
            sys.exit(-1)
        else:
            print("回滚版本请求发送执行成功,code:{},text:{}".format(response.status_code, response.text))
        return True, "版本回滚执行成功"
