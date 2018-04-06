#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
import sys,os,json,time

from conf import settings
from core import db_handler

def acc_auth(account,password):
    '''
    user account authrizetion;
    :param id: user id
    :param passwd: user password
    :return:
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    db_file = "%s/%s.json" %(db_path,account)
    print(settings.DATABASE)
    print(db_path)
    print(db_file)
    if os.path.isfile(db_file):
        with open(db_file,'r',encoding='utf8') as f:
            account_data = json.load(f)
            print(account_data)
def acc_login(user_data,log_obj):
    '''
    this is user login func,invoke acc_auth func has complish.
    :param user_data:user databases;
    :param log_obj:log write
    :return:
    '''
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3:
        print("\033[33;1m-------------Alex bank system----------\033[0m")
        account = input("\033[33;1muser name:\033[0m")
        password = input("\033[33;1mpassword:\033[0m")
        acc_auth(account,password)

