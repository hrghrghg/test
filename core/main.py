import sys,os
from core import auth

user_data = {
    "account_id":None,
    "is_authenticated":False,
    "account_data":None
}


def select():
    pass
def add():
    pass
def remove():
    pass
def transfer():
    pass
def withdraw():
    pass
def repay():
    pass
def frozen():
    pass
def printbill():
    pass

def run():
    print(menu)
    auth.acc_login(user_data,"test")
menu = u'''
------- Alex huang Bank ---------
\033[32;1m1.  账户信息
2.  添加账户
3.  注销账户
4.  转账
5.  提现
6.  冻结解冻
7.  返款
8.  打印账单
\033[0m'''
menu_dic = {
    "1":select,
    "2":add,
    "3":remove,
    "4":transfer,
    "5":withdraw,
    "6":frozen,
    "7":repay,
    "8":printbill
}
run()