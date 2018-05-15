#!_*_coding:utf-8_*_
#__author__:"Alex huang"

import threading,paramiko

class SSH_Threading(threading.Thread):
    def __init__(self,info):
        super(SSH_Threading,self).__init__()
        self.ip = info["ip"]
        self.port = info["port"]
        self.username = info["username"]
        self.password = info["password"]
        self.cmd = info["cmd"]
        self.action = info["action"]
        self.local = info["local"]
        self.remote = info["remote"]
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.ip,self.port,self.username,self.password)

    def run(self):
        stdin,stdout,stderr = self.ssh.exec_command(self.cmd)
        res = stdout.read()+stderr.read()
        print(res.decode())

class SFTP_Threading(threading.Thread):
    def __init__(self,info):
        super(SFTP_Threading,self).__init__()
        self.ip = info["ip"]
        self.port = info["port"]
        self.username = info["username"]
        self.password = info["password"]
        self.cmd = info["cmd"]
        self.action = info["action"]
        self.local = info["local"]
        self.remote = info["remote"]
        self.transfer = paramiko.Transport((self.ip,self.port))
        self.transfer.connect(username=self.username,password=self.password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transfer)

    def run(self):
        if hasattr(self.sftp,self.action):
            func = getattr(self.sftp,self.action)
            func(self.local,self.remote)


