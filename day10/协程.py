#!_*_coding:utf-8_*_
#__author__:"Alex huang"
# 手动切换
from greenlet import greenlet
def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()

def test2():
    print(56)
    gr1.switch()
    print(78)

if __name__ == '__main__':
    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    gr1.switch()

# 自动切换
import gevent
def func1():
    print("in the fun1..1")
    gevent.sleep(2)
    print("in the fun1..2")
def func2():
    print("in the fun2...1")
    gevent.sleep(1)
    print("in the fun2...2")
def func3():
    print("in the fun3...1")
    gevent.sleep(0)
    print("in the fun3...2")
gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    gevent.spawn(func3)
])
