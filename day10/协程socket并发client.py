#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg

import socket
sock = socket.socket()
sock.connect(('127.0.0.1',5000))
flag = False
while not flag:
    data = input(">>:").strip()
    if len(data) == 0:continue
    sock.send(data.encode())  #如果是发送一个空值，虽然显示是发出去了，但对方却认为你没发
    recv_data = sock.recv(8096)
    print("recv:",recv_data.decode())
sock.close()