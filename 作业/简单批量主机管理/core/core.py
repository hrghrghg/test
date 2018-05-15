#!_*_coding:utf-8_*_
#__author__:"Alex huang"

import optparse,configparser
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from ssh_threading import SSH_Threading,SFTP_Threading
db_file = os.path.join(BASE_DIR,"conf","host.ini")
def args():
    paser = optparse.OptionParser()
    paser.add_option("-H","--host",dest="host",help="specify host name")
    paser.add_option("-c","--cmd",dest="cmd",help="specify to do run instruction")
    paser.add_option("-a","--action",dest="action",help="specify to do run method")
    paser.add_option("-L","--local",dest="local",help="specify local host path")
    paser.add_option("-R","--remote",dest="remote",help="specify remote host path")
    (opt,args) = paser.parse_args()
    if opt.host == None or opt.cmd == None and opt.action == None:
        print("miss requre argument")
        exit(1)
    if opt.action and opt.cmd:
        print("-c and -a argument is diverged")
        exit(1)
    if opt.action:
        if not opt.local or not opt.remote:
            print("--local and --remote both exist")
            exit(1)
    return opt

def host_resolve(name):
    cnf = configparser.ConfigParser()
    cnf.read(db_file,encoding="utf-8")
    info = {}
    if name in cnf.sections():
        info["ip"] = cnf[name]["ip"]
        info["port"] = int(cnf[name]["port"])
        info["username"] = cnf[name]["username"]
        info["password"] = cnf[name]["password"]

        return info
    else:
        print("Host is not exist")
        exit(2)

if __name__ == '__main__':
    opt = args()
    host = opt.host.split(',')
    for i in host:
        ssh_info = host_resolve(i)
        ssh_info["cmd"] = opt.cmd
        ssh_info["action"] = opt.action
        ssh_info["local"] = opt.local
        ssh_info["remote"] = opt.remote
        if opt.cmd:
            t1 = SSH_Threading(ssh_info)
            t1.start()
        if opt.action:
            t1 = SFTP_Threading(ssh_info)
            t1.start()
        print(ssh_info)
