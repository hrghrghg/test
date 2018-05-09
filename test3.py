#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg

import getpass
password = getpass.getpass()
print(password)

# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='192.168.80.200',port=22,username='root',password='123')
# stdin,stdout,stderr = ssh.exec_command('df;top')
# res = stdout.read()+stderr.read()
# print(res.decode())

