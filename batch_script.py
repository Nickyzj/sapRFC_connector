from threading import Thread
import time
import batch_job.data_transfer as data_transfer
import batch_job.executeRFC as executeRFC

from batch_job.config import qcb, pcb, pb1, pw1

def callDataTransfer(sapConnection):
    print('callDataTransfer started...')
    while(True):
        data_transfer.main(sapConnection)
        time.sleep(60)

def callExecuteRFC(sapConnection):
    print('callExecuteRFC started...')
    while(True):
        executeRFC.main(sapConnection)
        time.sleep(5)



if __name__ == '__main__':
    sapConnections = []
    sapConnections.append(qcb)
    sapConnections.append(pcb)
    sapConnections.append(pb1)
    sapConnections.append(pw1)

    threadGroup = []
    for sapConnection in sapConnections:
        threadGroup.append(Thread(target=callDataTransfer, args=(sapConnection,)))
        threadGroup.append(Thread(target=callExecuteRFC, args=(sapConnection,)))

    for thead in threadGroup:
        thead.start()

    for thead in threadGroup:
        thead.join()