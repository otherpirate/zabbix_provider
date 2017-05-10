from pyzabbix import ZabbixAPI
from settings import ZABBIX_ENDPOINT, ZABBIX_USER, ZABBIX_PASSWORD

STATUS_ENABLED = 0
STATUS_DISABLED = 1


class ZabbixProvider(object):
    def __init__(self):
        self.api = ZabbixAPI(ZABBIX_ENDPOINT)
        self.api.login(ZABBIX_USER, ZABBIX_PASSWORD)

    def hosts_disabled(self, groups=None):
        return self.api.host.get(
            output=['hostid', 'name'],
            groupids=groups,
            filter={'status': STATUS_DISABLED},
        )

    def enable_host(self, host_id):
        return self.api.host.update(hostid=host_id, status=STATUS_ENABLED)

    def disable_host(self, host_id):
        return self.api.host.update(hostid=host_id, status=STATUS_DISABLED)

    def host_exist(self, host_name):
        response = self.api.host.get(
            output=['hostid', 'name'],
            filter={'host': host_name}
        )
        return response

    def __del__(self):
        self.api.user.logout()
