#!_*_coding:utf-8_*_
#__author__:"Alex huang"

import sys,os,socket,json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings
from core import core
from core import interactive

if __name__ == '__main__':
    attempt = 0
    while attempt < 3:
        print("\033[33;1m-------------login page-------------\033[0m")
        username = input("username:").strip()
        password = input("password:").strip()
        cmd_info = {
            "cmd":"login",
            "username":username,
            "password":password
        }
        conn = socket.socket()
        conn.connect((settings.servername,settings.port))
        conn.send(json.dumps(cmd_info).encode())
        recv_data = conn.recv(8096)
        if recv_data.decode() == "0":
            print("login success")
            interactive.interactive()
        elif recv_data.decode() == "1":
            print("password error")
        else:
            print("user is not exist")

        attempt += 1