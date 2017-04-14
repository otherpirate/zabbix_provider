# Zabbix Provider

Easy commands to use Zabbix API, like get information and do changes in your hosts/cloud

## Getting Started

Export your access variables:
```
export ZABBIX_ENDPOINT="http://api.zabbix.local.company/"
export ZABBIX_USER="api_user"
export ZABBIX_PASSWORD="user_password"
```

Download this project, install requirements.txt, then in python console:

```python
from provider import ZabbixProvider
provider = ZabbixProvider()
for host in provider.hosts_disabled():
  provider.enable_host(host_id=host['hostid'])
```

#ToDo: pypi

## Current Methods:

* hosts_disabled(groups=None) - Get all hosts with status 1, you can filter by groups
* enable_host(host_id) - Set host status to 0
* disable_host(host_id) - Set host status to 1

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
