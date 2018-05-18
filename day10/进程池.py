#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg

from multiprocessing import Process,Pool
import time,os
def bar(arg):
    print(arg[0],arg[1])  #返回的是元组参数
    print("process done...",arg,os.getpid())  #进程ID跟主进程 一样
def f(i):
    time.sleep(2)
    print("hello,world",i)
    return i,os.getpid()
if __name__ == '__main__':
    pool = Pool(3)
    print("主进程PID:",os.getpid())
    for i in range(10):
        #pool.apply(func=f,args=(i,))  #这是同步执行进程变串行了
        pool.apply_async(func=f,args=(i,),callback=bar)  #注意callback是叫回调函数，
        # 作用是每一个pool中的进程执行完成后，把返回值传给回调函数，bar再执行，这里bar一定不要带参数，会出错
        #可用在备份数据，完后写入一条记录，因为它是主进程调用执行的，所以节约代码和时间
    pool.close()       #close 在 join之前，一定要一起用，作用等待每个进程执行完
    pool.join()
    print("end...")

