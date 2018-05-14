#!_*_coding:utf-8_*_
#__author__:"Alex huang"

import threading,paramiko

class SSH_Threading(threading.Thread):
    def __init__(self,ip,port=22,username="root",password="123",cmd='ifconfig'):
        super(SSH_Threading,self).__init__()
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.cmd = cmd
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.ip,self.port,self.username,self.password)

    def run(self):
        stdin,stdout,stderr = self.ssh.exec_command(self.cmd)
        print(stdout.read().decode())

s1 = SSH_Threading("192.168.80.100",22,'root','123',"df")
s1.start()