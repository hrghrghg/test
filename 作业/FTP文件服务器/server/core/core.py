#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg

import socketserver
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
             while True:
                self.data = self.request.recv(1024).strip()
                print("Client IP:{}".format(self.client_address[0]))
                print(self.data)
                self.request.sendall(self.data.upper())
        except ConnectionResetError as e:
            print(e)
if __name__ == "__main__":
    HOST, PORT = "localhost", 6969
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
