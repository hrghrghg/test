#!_*_coding:utf-8_*_
#__author__:"Alex huang"
import multiprocessing,time,os
import threading

# print("主进程的父PID:",os.getppid())  #即pytharm进程ID
# print("主进程的PID:",os.getpid())

def sub(q):
    print("sub process")
    print("子进程的父PID:", os.getppid())
    print("子进程的PID:", os.getpid())
    q.send("aaa")
    q.send("bbb")
if __name__ == '__main__':
    pare_conn,chil_conn = multiprocessing.Pipe()
    t = multiprocessing.Process(target=sub,args=(chil_conn,))
    t.start()
    print(pare_conn.recv(),pare_conn.recv())
