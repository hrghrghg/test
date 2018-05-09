#!_*_coding:utf-8_*_
#__author__:"Alex huang"

import threading,time

import threading, time

def run(n):
    semaphore.acquire()
    print('threading in %s' %n)
    time.sleep(1)
    semaphore.release()
if __name__ == "__main__":
    semaphore = threading.BoundedSemaphore(5)
    for i in range(25):
        t = threading.Thread(target=run,args=(i,))
        t.start()
    while threading.active_count() != 1:
        pass
    else:
        print("All threading is done")