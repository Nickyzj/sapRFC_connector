from threading import Thread
import time
import batch_job.data_transfer as data_transfer
import batch_job.executeRFC as executeRFC


def callDataTransfer():
    print('callDataTransfer started...')
    while(True):
        data_transfer.main()
        time.sleep(60)

def callExecuteRFC():
    print('callExecuteRFC started...')
    while(True):
        executeRFC.main()
        time.sleep(5)


t1 = Thread(target = callDataTransfer, args=())
t2 = Thread(target = callExecuteRFC, args=())

t2.start()
t1.start()

t1.join()
t2.join()