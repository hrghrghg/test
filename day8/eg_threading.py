#!/usr/bin/env python
# -*- coding: utf8 -*-
# author aliex-hrg
import threading,time
lock = threading.Lock()
def run():
    lock.acquire()
    global num
    num += 1
    time.sleep(1)
    lock.release()
my_obj = []
num = 0
for i in range(50):
    t = threading.Thread(target=run)
    t.start()
    my_obj.append(t)

for j in my_obj:
    j.join()


print('sum',num)

