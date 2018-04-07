#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg

def add_credit():
    pass
def del_credit():
    pass
def frozen_credit():
    pass
manager_menu = u'''-------Alex Bank Manager System-------
\033[33;1m1.  add
2.  del
\033[0m'''


def manager():
    print("\033[33;1m-------Alex Bank Manager System-------\033[0m")
    user = input("\033[34;1mUser:\033[0m").strip()
    passwd = input("\033[34;1mPassword:\033[0m").strip()
    if user == "1" and passwd == "1":
        print("\033[33;1m-------Login Success-------\033[0m")


print(manager_menu)