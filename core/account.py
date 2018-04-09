#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
import json,sys,os
from conf import settings

def load_account_data(id):
    db_path = "%s/db/accounts" %settings.BASE_DIR
    file_path = "%s/%s.json" %(db_path,id)
    if os.path.isfile(file_path) is True:
        with open(file_path,'r',encoding='utf8') as f:
            return json.load(f)
def dump_account_data(user_data):
    '''
    user data write func
    :param user_data: 为子user data
    :return:
    '''
    db_path = "%s/db/accounts" %settings.BASE_DIR
    file_path = "%s/%s.json" %(db_path,user_data['id'])
    with open(file_path,'w',encoding='utf8') as f:
        json.dump(user_data,f)
        return True

def add_account_data(user_data):
    '''
    user data write func
    :param user_data: 为子user data
    :return:
    '''
    db_path = "%s/db/accounts" %settings.BASE_DIR
    file_path = "%s/%s.json" %(db_path,user_data['id'])
    if os.path.isfile(file_path) is not True:
        with open(file_path,'w',encoding='utf8') as f:
            json.dump(user_data,f)
            print("add success")
            return True
    else:print("credit is exist")