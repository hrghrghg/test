#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
import gevent
from gevent import socket
def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen(500)
    while True:
        conn,addr = s.accept()  #等待连接进来，没有连接一直挂起
        gevent.spawn(func,conn) #进来连接了，交给协程执行func函数，func无限收发数据，这中间遇到io切换
def func(conn):
    try:
        while True:
            recv = conn.recv(8096)
            print("recv:%s" %recv.decode())
            resp = recv.decode().upper()
            conn.send(resp.encode())
    except Exception as e:
        print(e)
    finally:
        conn.close()
if __name__ == '__main__':
    server(5000)

