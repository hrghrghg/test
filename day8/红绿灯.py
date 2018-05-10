#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg

import threading,time

event = threading.Event()

def redlight():
    event.set()
    count = 1
    while True:
        if count > 0 and count < 6:
            event.set()
            print("\033[44;1mGreen light...{}\033[0m".format(6 - count))
        elif count < 10:
            event.clear()
            print("\033[41;1mRed light...{}\033[0m".format(11 - count))
        else:
            print("\033[41;1mRed light...{}\033[0m".format(11 - count))
            count = 0
        count += 1
        time.sleep(1)
def car(name):
    while True:
        if event.is_set():
            print("\033[34;1m%s is running...\033[0m" %name)
        else:
            print("\033[31;1m%s is stop...\033[0m" % name)
            event.wait()     #程序走到这儿，如果event没有被set，会一直等待，直到被set了才会继续向下运行
        time.sleep(1)

run = threading.Thread(target=redlight)
run.start()
car1 = threading.Thread(target=car,args=("car1",))
car1.start()
car2 = threading.Thread(target=car,args=("car2",))
car2.start()
car3 = threading.Thread(target=car,args=("car3",))
car3.start()