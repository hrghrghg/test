#!/usr/bin/env python
# -*- coding: utf8 -*-
# author aliex-hrg

import paramiko

private_key = paramiko.RSAKey.from_private_key_file( 'C:\\Users\\HRG\\Desktop\\hrg_tools\\key-files\\id_Alex_huang','hrg2,,2617')
transparent = paramiko.Transport(('218.90.200.48',22))
transparent.connect(username='hrg',pkey=private_key)
sftp = paramiko.SFTPClient.from_transport(transparent)
sftp.get('/home/hrg/1','1')
sftp.put('test.py','/home/hrg/2')




# ssh =  paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='218.90.200.48',port=22,username='hrg',pkey=private_key)
# stdin, stdout, stderr = ssh.exec_command('ls -a')
# result = stdout.read()+stderr.read()
# print(result.decode())
# ssh.close()