bw_monitor_host = 'http://localhost:5000'

class SAPConnection:

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

