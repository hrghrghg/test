#!_*_coding:utf-8_*_
#__author__:"Alex huang"
import json,hashlib
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

def help():
    msg = '''-------- Support following command --------
    put     get     ls      cd      
    pwd     help'''
    print('\033[34;1m%s\033[0m' %msg)
def interactive(conn,username):
    print('\033[33;1m-----------Welcome to HRG FTP SERVER------------\033[0m')
    help()
    while True:
        cmd = input(">>:").strip()
        if not len(cmd):continue
        cmd_list = cmd.split()
        info_dict = {"user":username}    #为传递给服务器的命令 用户 参数 字典信息
        i = 0     #用以区别多少个参数的下标
        for line in cmd_list:
            if i == 0:
                info_dict["cmd"] = line
            else:
                info_dict["par%s" %i] = line
            i += 1
        print('cmd',info_dict)
        conn.send(json.dumps(info_dict).encode())   #将执行命令json化发送给服务器
        if info_dict["cmd"] == "get":

            filesize = int(conn.recv(1024).decode())
            if filesize != 0:
                m = hashlib.md5()
                filenum = 0
                progress = 0
                print(filesize)
                conn.send(b"ack")  #消除粘包
                if info_dict.get('par1'):
                    with open(info_dict['par1'],'wb') as f:
                        while filenum != filesize:
                            data = conn.recv(8096)
                            f.write(data)
                            filenum += len(data)
                            modulus = (len(data)+progress)//(filesize/100)  #把一次读取到的大小按文件总大小除100取模，并打印模个点
                            if modulus >= 1.0:progress = 0    #如果模为0，累计到下次，直到模为1，并清除累计值
                            progress = (len(data)+progress)%(filesize/100)    #余数 累计值
                            for i in range(int(modulus)):    #for打印一次模的点数
                                sys.stdout.write('.')
                                sys.stdout.flush()
                            percent = int(100*filenum/filesize)
                            show_str = "[%-100s] %s%%" %(percent*'#',percent)
                            print('\r%s' %show_str,file=sys.stdout,flush=True,end='')
                            # print("{:.2f}%".format(filenum/filesize*100))
                            # print('sum:',filenum,'curr:',len(data))

        re_data = conn.recv(8096).decode()
        print(re_data)