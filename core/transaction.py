#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg

import sys,os,json,time
from conf import settings
from core import account

def transaction(acc_data,trans_type,amount,**kwargs):
    '''
    this is contain withdraw,transcation,repyment func
    :param acc_data: account data
    :param trans_type: trade type
    :param amount: trade number
    :param kwargs: transfer others parmeters
    :return:
    '''
    interest = settings.TANSACTION_TYPE[trans_type]['interest']
    old_balance = acc_data['balance']
    if trans_type in settings.TANSACTION_TYPE:
        if settings.TANSACTION_TYPE[trans_type]['action'] == "plus":
            new_balance = old_balance + amount + amount * interest
        elif settings.TANSACTION_TYPE[trans_type]['action'] == "minus":
            new_balance = old_balance - amount - amount * interest
            if new_balance < 0:
                print("余额不够")
                return "fail"
        acc_data['balance'] = new_balance
        return account.dump_account_data(acc_data)
    else:
        print("此操作不支持")