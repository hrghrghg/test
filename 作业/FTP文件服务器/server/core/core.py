#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg

import sys,os,socketserver,json,hashlib
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings
import admin

class MyTCPHandler(socketserver.BaseRequestHandler):
    ftp_dir = settings.HOME_DIR     #定义FTP服务器根目录
    curr_dir = None     #定义用户当前目录
    def ls(self,info):
        print('bug:',self.curr_dir)
        if not info.get('par1'):
            cmd = 'dir %s' %self.curr_dir
            user_data = os.popen(cmd).read()
            return user_data
        else:
            path_dir = info["par1"]
            cmd = 'dir %s\%s' %(self.curr_dir,path_dir)
            user_data = os.popen(cmd).read()
            return user_data

    def pwd(self,info):
        pwd_dir = [i for i in self.curr_dir.split("D:\\ftp\%s" %info['user']) if i]
        if len(pwd_dir) == 0:
            pwd_dir.append('\\')
        return pwd_dir[0]

    def cd(self,info):
        username = info['user']
        exist_dir = os.popen("dir %s" %self.curr_dir).read()
        if not info.get('par1'):
            self.curr_dir = '%s\%s' % (self.ftp_dir, username)
            print('curr_dir',self.curr_dir)
            return self.curr_dir
        else:
            path_dir = info["par1"]
            if path_dir in exist_dir:
                self.curr_dir = '%s\%s' % (self.curr_dir,path_dir)
                return self.curr_dir
            else:
                return "this directory is not exist"
    def login(self,info):
        if info.get('par1') and info.get('par2'):
            username = info["par1"]
            password = info["par2"]
            login_status = admin.login(username, password)
            if login_status == 0:
                self.curr_dir = '%s\%s' % (self.ftp_dir, username)
            return str(login_status)
        else:
            return 3
    def get(self,info):
        if info.get('par1'):
            file_path = "%s\%s" %(self.curr_dir,info['par1'])
            if os.path.isfile(file_path):
                filesize = os.stat(file_path).st_size
                m = hashlib.md5()
                self.request.sendall(str(filesize).encode())  #发送文件大小
                self.request.recv(1024)  #消除粘包

                with open(file_path,'rb') as f:
                    for line in f:
                        self.request.send(line)
                        m.update(line)
                file_md5 = m.hexdigest()
                return "download success"
            else:
                self.request.send(b'0')
                print("file does not exist")
                return "file does not exist"
        else:
            self.request.send(b'0')
            print("miss a request parameters")
            return "miss a request parameters"
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

        except ConnectionResetError as e:
            print(e)
if __name__ == "__main__":
    HOST, PORT = settings.servername,settings.port
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
