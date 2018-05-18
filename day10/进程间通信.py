#!_*_coding:utf-8_*_
#__author__:"Alex huang"
from multiprocessing import Process,Manager
import threading,time,os

def sub(d,l):
    d[os.getpid()] = os.getpid()
    l.append(os.getppid())
    print(l)
    #print(d)
if __name__ == '__main__':
    with Manager() as M: #with..as的作用是把Manager()生成一个别名M,并只有在with内有效
        d = M.dict()    #用了with,下面也可以不用。
        l = Manager().list(range(5))
        p_list = []    #这个列表保存生成的多个进程 ，方便促一join()。等待全部完成，
        for i in range(10):
            t = Process(target=sub,args=(d,l))
            t.start()
            p_list.append(t)
        for i in p_list:
            i.join()
        print(d,l)