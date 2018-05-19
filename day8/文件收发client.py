#!/usr/bin/env python
#-*-coding:utf-8 -*-
# author aliex-hrg
import socket,os,hashlib

sock = socket.socket()
sock.connect(('localhost',6969))
flag = False
while flag is not True:
    content = input(">>:").strip()
    cmd,filename = content.split()
    if content == "b":flag = True
    if len(content) == 0:continue
    if content.startswith('get'):
        sock.send(content.encode())

        file_size = int(sock.recv(1000).decode())
        print('file_size:',file_size)
        sock.send(b'ack')
        m = hashlib.md5()
        recv_size = 0
        with open('filename','wb') as f:
            while recv_size != file_size:
                data = sock.recv(8096)
                recv_size += int(len(data))
                f.write(data)
                m.update(data)
        md5 = m.hexdigest()
        sock.send(b'ack')
        recv_md5 = sock.recv(1024).decode()
        if md5 != recv_md5:
            print('file transfer error')
sock.close()