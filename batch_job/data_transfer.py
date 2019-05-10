import requests
import json
import pyrfc
from batch_job.config import user, ashost, sysnr, client, passwd
from batch_job.config import bw_monitor_host

def getData():
    conn_bw = pyrfc.Connection(ashost=ashost, sysnr=sysnr, client=client, user=user, passwd=passwd)

    T_ZCHAIN_AF_INFO = ''
    T_ZCHAIN_AF_LOG = ''
    result = ''
    chain_monitor_rfc = conn_bw.call('ZCHAIN_MONITOR',
                                     I_LOG_DATE='20190401',
                                     T_ZCHAIN_AF_INFO=T_ZCHAIN_AF_INFO)

    conn_bw.close()
    return chain_monitor_rfc['T_ZCHAIN_AF_INFO']


def main():
    try:
        data = json.dumps(getData())
    except pyrfc._exception.CommunicationError as e:
        print(e)

    try:
        r = requests.post(bw_monitor_host + '/data/upload', json = data)
        # print(r.text)
    except requests.exceptions.ConnectionError as e:
        print(e)
    except requests.exceptions.Timeout as e:
        print(e)

if __name__ == '__main__':
    main()