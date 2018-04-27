#!_*_coding:utf-8_*_
#__author__:"Alex huang"

def help():
    msg = '''-------- Support following command --------
    put     get     ls      cd      
    pwd     help'''
    print('\033[34;1m%s\033[0m' %msg)
def interactive():
    print('\033[33;1m-----------Welcome to HRG FTP SERVER------------\033[0m')
    help()
    cmd = input(">>:")