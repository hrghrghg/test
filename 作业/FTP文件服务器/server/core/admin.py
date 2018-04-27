#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg

import sys,os,json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings
def useradd():
    username = input("username:").strip()
    password = input("password:").strip()
    limit = input("limit:").strip()
    info = {"username":username,"passwd":password,"limit":limit,"tra_status":None}
    user_file = "%s\conf\%s.json" %(BASE_DIR,username)
    with open(user_file,'w',encoding='utf-8') as f:
        json.dump(info,f)
        print("create user success")
def userdel():
    pass
def login(user,passwd):
    file_path = "%s\conf\%s.json" %(BASE_DIR,user)
    if os.path.isfile(file_path):
        with open(file_path,'r',encoding='utf-8') as f:
            data = json.load(f)
            if passwd == data['passwd']:
                print('\033[31;1mlogin success\033[0m')
                return 0
            else:
                print("\033[31;1mpassword error\033[0m")
                return 1
    else:
        print("\033[31;1muser not exist\033[0m")
        return 2
menu = '''---------user admin-------
    1. add user
    2. del user
'''
menu_dict = {
    "1":useradd,
    "2":userdel
}

if __name__ == '__main__':
    print("\033[31;1m-----admin login-----\033[0m")
    username = input("username:").strip()
    password = input("password:").strip()
    if login(username,password):
        while True:
            print("\033[32;1m%s\033[0m" %menu)
            choice = input(">>:").strip()
            if choice == "q":
                break
            if not choice or choice not in menu_dict:
                continue
            menu_dict[choice]()
