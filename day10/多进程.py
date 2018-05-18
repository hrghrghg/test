#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg

import multiprocessing,time,threading,os

print(os.getppid())
print(os.getpid())
def thread_run(n):
    print("run in threading...",n)
def run(n):
    print("process %s" %n,multiprocessing.current_process())
    t = threading.Thread(target=thread_run,args=(n,))
    t.start()
    print(os.getppid())
    print(os.getpid())
    time.sleep(2)

if __name__ == '__main__':
    for i in range(10):
        t = multiprocessing.Process(target=run,args=(i,))
        t.start()
