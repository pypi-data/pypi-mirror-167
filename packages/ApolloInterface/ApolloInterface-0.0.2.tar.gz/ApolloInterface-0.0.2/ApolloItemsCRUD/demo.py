from ApolloItemsCRUD.apolloService import ApolloUpdate



def test_CRUD():
    items_data = [
        {"action": "create", "apps": "automation", "namespaces": "common", "key": "test.testt.nm1", "value": "123", "clusters": "default","env": "PRO"},
        {"action": "create", "apps": "automation", "namespaces": "common", "key": "test.testt.nm2", "value": "123", "clusters": "default","env": "PRO"},
        {"action": "create", "apps": "automation", "namespaces": "common", "key": "test.testt.nm3", "value": "123", "clusters": "default","env": "PRO"},
        {"action": "create", "apps": "cmdb", "namespaces": "Test", "key": "nm1", "value": "123", "clusters": "default","env": "PRO"},
        {"action": "create", "apps": "cmdb", "namespaces": "Test", "key": "nm2", "value": "123", "clusters": "default","env": "PRO"},
        {"action": "create", "apps": "cmdb", "namespaces": "Test", "key": "nm3", "value": "123", "clusters": "default","env": "PRO"},
        {"action": "create", "apps": "platform", "namespaces": "T1", "key": "nm1", "value": "123", "clusters": "default","env": "PRO"},
        {"action": "create", "apps": "platform", "namespaces": "T1", "key": "nm2", "value": "123", "clusters": "default","env": "PRO"},
        {"action": "create", "apps": "platform", "namespaces": "T1", "key": "nm3", "value": "123", "clusters": "default","env": "PRO"},
        {"action": "create", "apps": "platform", "namespaces": "T2", "key": "nm1", "value": "123", "clusters": "default","env": "PRO"},
        {"action": "create", "apps": "platform", "namespaces": "T2", "key": "a2", "value": "123", "clusters": "default","env": "PRO"},
        {"action": "create", "apps": "platform", "namespaces": "T2", "key": "w3", "value": "123", "clusters": "default","env": "PRO"},

    ]

    # items_data = json.loads(items_data, encoding='utf-8')
    apollo = ApolloUpdate(addr, name, password)
    version = apollo.main_CRUD2(items_data)
    print(version)


def test_rollback():
    apps = 'platform'
    namespace = 'T1'
    release_version = "20220902141720_release_by_automation"
    env = "PRO"
    cluster = "default"

    apollo = ApolloUpdate(addr, name, password)
    version = apollo.main_rollback(release_version, apps, namespace, env, cluster)


addr = '10.1.1.1:7547'
name = 'apollo'
password = 'Apollo@086)*^'
version_cache_dir = r'\tmp\backUpApolloVersion'
if __name__ == '__main__':
    # items_data = json.loads(items_data, encoding='utf-8')
    # apollo = ApolloUpdate(addr, name, password)
    # flag,version = apollo.main_CRUD2(items_data,version_cache_dir)
    # if not flag:
    #     ExitCode = -1
    # apollo = ApolloUpdate(addr, name, password)
    # version = apollo.main_rollback(release_version, apps, namespace, env, cluster)
    test_CRUD()
    # test_rollback()
