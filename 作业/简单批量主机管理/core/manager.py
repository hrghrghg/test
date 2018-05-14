#!_*_coding:utf-8_*_
#__author__:"Alex huang"

import sys,os
import configparser
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings

def host_add(name,ip,port=22,username='root',password='123'):
    config_old = configparser.ConfigParser()
    config_old.read(os.path.join(settings.DB_PATH,'host.ini'))
    config_new = configparser.ConfigParser()
    if name not in config_old.sections():
        config_new.add_section(name)
        config_new[name] = {
            "ip":ip,
            "port":port,
            "username":username,
            "password":password
        }
        config_new.write(open(os.path.join(settings.DB_PATH,'host.ini'),'a',encoding='utf-8'))
    else:
        print("this host is exist!")



