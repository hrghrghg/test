#!/usr/bin/env python
# -*- coding: utf8 -*-
# author aliex-hrg
import threading,time
star_time = time.time()
def run1(n,k):
    print(n)
    time.sleep(k)
    print('run done...',n)
t1 = threading.Thread(target=run1,args=("t1",1))
t1.setDaemon(True)
t1.start()
t2 = threading.Thread(target=run1,args=("t2",2))
t2.setDaemon(True)
t2.start()
#t2.join()

class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread,self).__init__()
        self.n = n
    def run(self):      #这里函数名必须是叫run
        print("run in thread...",self.n,threading.active_count())
        time.sleep(2)
my_obj = []
for i in range(4):
    name = MyThread(i);
    name.setDaemon(True)
    name.start()
    my_obj.append(name)



print('-----main threading------')
print("cost:",time.time() - star_time)
