#!/usr/bin/env python
# -*- coding: utf8 -*-
# author aliex-hrg

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.80.100',22,'root','123')
stdin,stdout,stderr = ssh.exec_command('echo $PATH')
print(stdout.read().decode())