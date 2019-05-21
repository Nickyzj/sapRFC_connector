import requests
import json
import pyrfc
from batch_job.config import qcb
from batch_job.config import bw_monitor_host
from datetime import datetime, timedelta, date

def getYesterday(day_diff=3):
    return (datetime.today() - timedelta(days=day_diff)).strftime("%Y%m%d")

def getData(sapConnection):
    conn_bw = pyrfc.Connection(ashost=sapConnection.ashost,
                               sysnr=sapConnection.sysnr,
                               client=sapConnection.client,
                               user=sapConnection.user,
                               passwd=sapConnection.passwd)

    T_ZCHAIN_AF_INFO = ''
    T_ZCHAIN_AF_LOG = ''
    chain_monitor_rfc = conn_bw.call('ZCHAIN_MONITOR',
                                     I_LOG_DATE=getYesterday(),
                                     T_ZCHAIN_AF_INFO=T_ZCHAIN_AF_INFO)

    conn_bw.close()
    return chain_monitor_rfc['T_ZCHAIN_AF_INFO']


def main(sapConnection):
    try:
        data = json.dumps(getData(sapConnection))
        if data is None:
            print("Data is None.")
            return
        r = requests.post(bw_monitor_host + '/data/upload/' + sapConnection.name, json = data)
    except pyrfc._exception.CommunicationError as e:
        print(e)
    except requests.exceptions.ConnectionError as e:
        print(e)
    except requests.exceptions.Timeout as e:
        print(e)

if __name__ == '__main__':
    main(qcb)