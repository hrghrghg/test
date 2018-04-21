import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import auth
from core import account
from core import manager
from core import transaction
user_data = {
    "account_id":None,
    "is_authenticated":False,
    "account_data":None
}


def credit_info(acc_data):
    print(account.load_account_data(acc_data['account_id']))
def transfer(acc_data):
    acc_data = account.load_account_data(acc_data['account_id'])
    exit_flag = False
    while not exit_flag:
        acc_data = account.load_account_data(acc_data['id'])
        curr_info = '''------------ Alex Bank ------------
        Credit:%s
        Balance:%s''' % (acc_data['id'], acc_data['balance'])
        print("\033[33;1m%s\033[0m" %curr_info)
        to_credit = input("\033[34;1m对方账号>>:\033[0m")
        amount = input("\033[34;1m转账金额>>:\033[0m").strip()
        to_acc_data = account.load_account_data(to_credit)
        if len(amount) > 0 and amount.isnumeric():
            amount = float(amount)
            ack = transaction.transaction(acc_data,'transfer',amount)
            ack2 = transaction.transaction(to_acc_data,'repay',amount)
            if ack == "True" and ack2 == "True":
                print("transfer success")
        if amount == "b":
            exit_flag = True
def withdraw(acc_data):
    acc_data = account.load_account_data(acc_data['account_id'])
    exit_flag = False
    while not exit_flag:
        acc_data = account.load_account_data(acc_data['id'])
        curr_info = '''------------ Alex Bank ------------
        Credit:%s
        Balance:%s''' % (acc_data['id'], acc_data['balance'])
        print("\033[33;1m%s\033[0m" %curr_info)
        amount = input("\033[34;1m>>:\033[0m").strip()
        if len(amount) > 0 and amount.isnumeric():
            amount = float(amount)
            ack = transaction.transaction(acc_data,'withdraw',amount)
            if ack == "True":
                print("transfer success")
        if amount == "b":
            exit_flag = True
def repay(acc_data):
    acc_data = account.load_account_data(acc_data['account_id'])
    exit_flag = False
    while not exit_flag:
        acc_data = account.load_account_data(acc_data['id'])
        curr_info = '''------------ Alex Bank ------------
        Credit:%s
        Balance:%s''' % (acc_data['id'], acc_data['balance'])
        print("\033[33;1m%s\033[0m" %curr_info)
        amount = input("\033[34;1m>>:\033[0m").strip()
        if len(amount) > 0 and amount.isdigit():
            amount = float(amount)
            ack = transaction.transaction(acc_data,'repay',amount)
            if ack == "True":
                print("repay success")
        if amount == "b":
            exit_flag = True
def showbill():
    pass

def run():
    acc_data = auth.acc_login(user_data,"test")
    user_data['account_data'] = acc_data
    interactive(user_data)
def interactive(acc_data):
    '''
    this is a interactive func,contain withdraw,transfer,frozen etc
    :param acc_data:user account data
    :return:
    '''
    menu = u'''
    ------- Alex huang Bank ---------
    \033[32;1m1.  账户信息
    2.  转账
    3.  提现
    4.  返款
    5.  打印账单
    6.  管理界面
    7.  退出
    \033[0m'''
    menu_dic = {
        "1":credit_info,
        "2":transfer,
        "3":withdraw,
        "4":repay,
        "5":showbill,
        "6":manager.manager,
        "7":exit
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        choise = input(">>>:").strip()
        if choise in menu_dic:
            menu_dic[choise](acc_data)
        else:
            print("\033[31;1m此选择不存在\033[0m")

run()