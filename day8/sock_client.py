#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg

import socket
sock = socket.socket()
# server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#sock.connect(('120.78.197.182',51102))
sock.connect(('localhost',6969))
flag = False
while not flag:
    data = input(">>:").strip()
    if data == "b":flag = True
    if len(data) == 0:continue
    sock.send(data.encode())
    recv_data = sock.recv(8096)
    print("recv:",recv_data.decode())

    # recv_data = b''
    # recv_len = 0
    # cmd_length = int(sock.recv(8096).decode())
    # cli_ack = sock.send(b'ack')
    # print('cmd_len',cmd_length)
    # while recv_len != cmd_length:
    #     data = sock.recv(1024)
    #     recv_data += data
    #     recv_len += len(data)
    # print('recv:',recv_data.decode())
sock.close()