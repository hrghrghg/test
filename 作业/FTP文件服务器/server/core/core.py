#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg

import sys,os,socketserver,json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings
import admin

class MyTCPHandler(socketserver.BaseRequestHandler):
    ftp_dir = settings.HOME_DIR     #定义FTP服务器根目录
    def ls(self,info):
        username = info["user"]
        if len(info) == 2:
            curr_dir = 'dir %s\%s' %(self.ftp_dir,username)
            user_data = os.popen(curr_dir).read()
            return user_data
        else:
            path_dir = info["par1"]
            curr_dir = 'dir %s\%s\%s' %(self.ftp_dir,username,path_dir)
            user_data = os.popen(curr_dir).read()
            return user_data
    def login(self,info):
        if len(info) < 3:return 3
        username = info["par1"]
        password = info["par2"]
        login_status = admin.login(username, password)
        return str(login_status)

    def handle(self):
        try:
            while True:
                data = self.request.recv(1024) #获取用户提交的命令和参数
                if not data:break
                print("Client IP:{}".format(self.client_address[0]))
                recv_data = json.loads(data.decode())
                print('cmd:',recv_data)
                if hasattr(MyTCPHandler,recv_data["cmd"]):
                    func = getattr(MyTCPHandler,recv_data["cmd"])   #反射函数并执行
                    msg = func(self,recv_data)
                    print('cmd_result:',msg)
                    if not len(msg):msg = "Command Error,Pls Retype"
                    self.request.sendall(msg.encode())  #返回正常执行结果给客户端
                else:
                    print("this command is not support")
                    self.request.sendall(b'this command is not support')   #返回错误执行结果给客户端
                # print("recv_data:",recv_data)
                # if recv_data['cmd'] == "login":
                #     MyTCPHandler.login(self,recv_data)

        except ConnectionResetError as e:
            print(e)
if __name__ == "__main__":
    HOST, PORT = settings.servername,settings.port
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
