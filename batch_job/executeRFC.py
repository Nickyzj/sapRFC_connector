import requests
import json
import pyrfc
from rfc_connection.qcb import user, ashost, sysnr, client, passwd
from batch_job.config import bw_monitor_host


def rfcCall(item):
    try:
        conn_bw = pyrfc.Connection(ashost=ashost, sysnr=sysnr, client=client, user=user, passwd=passwd)
        result = conn_bw.call(item['rfcName'],
                              I_LOGID = item['LOG_ID'],
                              I_CHAIN = item['CHAIN_ID'],
                              I_TYPE = item['TYPE'],
                              I_VARIANT = item['VARIANTE'],
                              I_INSTANCE = item['INSTANCE'],
                              I_JOB_COUNT = item['JOB_COUNT'])
        conn_bw.close()
    except Exception as e:
        print(e)
        return '{"error": "' + str(e) + '"}'
    else:
        return result

def main():
    try:
        r = requests.get(bw_monitor_host + '/data/execute')
        print(r.json())
        data = json.loads(r.text)
        if data.get('rfcName') not in rfcNameList:
            print('List is empty.')
        else:
            returnMsg = rfcCall(data)
            r = requests.post(bw_monitor_host + '/data/execute/status', json = returnMsg)
            print(r.text)

    except requests.exceptions.ConnectionError as e:
        print(e)
    except requests.exceptions.Timeout as e:
        print(e)

rfcNameList = ['ZCHAIN_REMOVE_INVALID_CHAR', 'ZCHAIN_ACTIVATE_TR_DTP', 'ZCHAIN_STEP_REPEAT', 'ZCHAIN_IGNORE_VARIANT']

if __name__ == '__main__':
    main()