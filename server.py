#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author aliex-hrg
import socket,os,hashlib

sock = socket.socket()
sock.bind(('localhost',6969))
sock.listen()
print("kai shi le")
conn,addr = sock.accept()
while True:
    data = conn.recv(8096).decode()
    print('recv:',data)
    m = hashlib.md5()
    cmd,filename = data.split()
    if os.path.isfile(filename):
        filesize = os.stat(filename).st_size
        conn.send(str(filesize).encode())
        conn.recv(1024)
        with open(filename,'rb') as f:
            for line in f:
                conn.send(line)
                m.update(line)
        md5 = m.hexdigest()
        conn.recv(1024)
        conn.send(md5.encode())
    else:
        print("file is not exist")
        conn.close()
        conn,addr = sock.accept()
