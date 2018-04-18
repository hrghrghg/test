#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
import sys,os,time,json
from core import account
from conf import settings
def add_credit():
    id = input("id:")
    password = input("password:")
    balance = input("balance:")
    temp_data = {
        "status": 0,
        "password": password,
        "pay_day": 22,
        "balance": float(balance),
        "expire_date": "2021-01-01",
        "credit": 15000,
        "enroll_date": "2016-01-02",
        "id": id
    }
    account.add_account_data(temp_data)
def del_credit():
    id = input("请输入删除用户：")
    file_path = "%s/db/accounts/%s.json" %(settings.BASE_DIR,id)
    if os.path.isfile(file_path):
        os.remove(file_path)
        print("删除成功")
        return True
def frozen_credit():
    pass
manager_menu = u'''\033[33;1m1.  添加信用卡
2.  注销信用卡
3.  冻结解冻
4.  退出\033[0m'''
manager_menu_dic = {
    "1":add_credit,
    "2":del_credit,
    "3":frozen_credit,
    "4":exit
}


def manager(*args):
    print("\033[33;1m-------Alex Bank Manager System-------\033[0m")
    user = input("\033[34;1mUser:\033[0m").strip()
    passwd = input("\033[34;1mPassword:\033[0m").strip()
    if user == "1" and passwd == "1":
        print("\033[33;1m-------Login Success-------\033[0m")
        while True:
            print(manager_menu)
            choise = input(">>>:")
            manager_menu_dic[choise]()
    else:
        print("\033[31;1m密码或用户名不对\033[0m")

