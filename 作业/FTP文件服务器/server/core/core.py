#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg

import sys,os,socketserver
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings

class MyTCPHandler(socketserver.BaseRequestHandler):
    ftp_dir = 'd:/ftp'
    def ls(self,path_dir):
        user_data = os.popen('ls')


    def handle(self):
        try:
             while True:
                self.data = self.request.recv(1024).strip()
                if not self.data:break
                print("Client IP:{}".format(self.client_address[0]))
                print(self.data)
                self.request.sendall(self.data.upper())
        except ConnectionResetError as e:
            print(e)
if __name__ == "__main__":
    HOST, PORT = settings.servername,settings.port
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
