#!_*_coding:utf-8_*_
#__author__:"Alex huang"

import sys,os,socket
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings
def conn():
    sock = socket.socket()
    sock.connect((settings.servername,settings.port))
    flag = False
    while not flag:
        data = input(">>:").strip()
        if data == "exit":flag = True
        if len(data) == 0:continue
        cmd_info = data.split()

        sock.send(cmd_info[0].encode())
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