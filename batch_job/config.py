import json

bw_monitor_host = 'http://localhost:5000'

class SAPConnection:

    @classmethod
    def from_json(cls, json_data):
        dict = json.loads(json_data)
        return SAPConnection(dict['name'], dict['user'], dict['ashost'], dict['sysnr'], dict['client'], dict['passwd'])

    def __init__(self, name, user, ashost, sysnr, client, passwd):
        self.name = name
        self.user = user
        self.ashost = ashost
        self.sysnr = sysnr
        self.client = client
        self.passwd = passwd



import rfc_connection.qcb as qcb_config

qcb = SAPConnection(name = 'qcb',
                    user = qcb_config.user,
                    ashost = qcb_config.ashost,
                    sysnr = qcb_config.sysnr,
                    client = qcb_config.client,
                    passwd = qcb_config.passwd)

import rfc_connection.pcb as pcb_config

pcb = SAPConnection(name = 'pcb',
                    user = pcb_config.user,
                    ashost = pcb_config.ashost,
                    sysnr = pcb_config.sysnr,
                    client = pcb_config.client,
                    passwd = pcb_config.passwd)

import rfc_connection.pb1 as pb1_config

pb1 = SAPConnection(name = 'pb1',
                    user = pb1_config.user,
                    ashost = pb1_config.ashost,
                    sysnr = pb1_config.sysnr,
                    client = pb1_config.client,
                    passwd = pb1_config.passwd)

import rfc_connection.pw1 as pw1_config

pw1 = SAPConnection(name = 'pw1',
                    user = pw1_config.user,
                    ashost = pw1_config.ashost,
                    sysnr = pw1_config.sysnr,
                    client = pw1_config.client,
                    passwd = pw1_config.passwd)