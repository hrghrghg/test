#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg

import sys,os,socketserver,json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings
import admin

class MyTCPHandler(socketserver.BaseRequestHandler):
    ftp_dir = 'd:/ftp'
    def ls(self,path_dir):
        user_data = os.popen('ls %s' %path_dir).read()
        return user_data
    def login(self,info):
        username = info['password']
        password = info["username"]
        self.login_status = admin.login(username, password)
        self.login_status = str(self.login_status)
        self.request.sendall(self.login_status.encode())

    def handle(self):
        try:
             while True:
                self.data = self.request.recv(1024).strip()
                if not self.data:break
                print("Client IP:{}".format(self.client_address[0]))
                recv_data = json.loads(self.data.decode())  #获取用户提交的命令和参数
                print("recv_data:",recv_data)
                if recv_data['cmd'] == "login":
                    MyTCPHandler.login(self,recv_data)


        except ConnectionResetError as e:
            print(e)
if __name__ == "__main__":
    HOST, PORT = settings.servername,settings.port
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
