import pyrfc

from rfc_connection.qcb import user, passwd, ashost, sysnr, client

rfcConnection = pyrfc.Connection(ashost=ashost, sysnr=sysnr, client=client, user=user, passwd=passwd)
print("SAP RFC [QCB] connected.")

def getData():
    conn_bw = rfcConnection

    T_ZCHAIN_AF_INFO = ''
    T_ZCHAIN_AF_LOG = ''
    chain_monitor_rfc = conn_bw.call('ZCHAIN_MONITOR',
                                     I_LOG_DATE='20190401',
                                     T_ZCHAIN_AF_INFO=T_ZCHAIN_AF_INFO)
    return chain_monitor_rfc['T_ZCHAIN_AF_INFO']

def rfcCall(rfcName, item):
    conn_bw = rfcConnection
    result = conn_bw.call(rfcName,
                          I_LOGID = item['LOG_ID'],
                          I_CHAIN = item['CHAIN_ID'],
                          I_TYPE = item['TYPE'],
                          I_VARIANT = item['VARIANTE'],
                          I_INSTANCE = item['INSTANCE'],
                          I_JOB_COUNT = item['JOB_COUNT'])
    return result