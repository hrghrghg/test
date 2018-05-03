#!_*_coding:utf-8_*_
#__author__:"Alex huang"
import json,hashlib
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
def to_get(conn,info_dict):
    if not info_dict.get('par1'): return "miss parameter"
    filesize = int(conn.recv(1024).decode())
    if filesize != 0:
        m = hashlib.md5()
        filenum = 0
        print(filesize)
        if os.path.isfile(info_dict['par1']+'.tmp'):
            has_size = os.stat(info_dict['par1']+'.tmp').st_size
            conn.send(str(has_size).encode())  # 消除粘包并传送已经接收文件大小
            filesize -= has_size
        else:
            conn.send(b'0')
        with open(info_dict['par1'] + '.tmp', 'ab') as f:
            while filenum != filesize:
                data = conn.recv(8096)
                f.write(data)
                m.update(data)
                filenum += len(data)
                # print('sum:', filenum, 'curr:', len(data))
                percent = int(100 * filenum / filesize)
                show_str = "[%-100s] %s%%" % (percent * '#', percent)
                print('\r%s' % show_str, file=sys.stdout, flush=True, end='')
        conn.send(b"ack")  # 消除粘包
        recv_md5 = conn.recv(1024)
        conn.send(b"ack")  # 消除粘包
        if recv_md5.decode() == m.hexdigest():
            if os.path.isfile(info_dict['par1']):
                os.remove(info_dict['par1'])
            os.rename(info_dict['par1'] + '.tmp',info_dict['par1'])
        else:
            print("file transfer error")

def to_put(conn,info_dict):
    if not info_dict.get('par1'):return "miss parameters"
    file_path = info_dict['par1']
    m = hashlib.md5()
    conn.recv(1024) # 消除粘包
    if os.path.isfile(file_path):
        filesize = os.stat(file_path).st_size
        conn.sendall(str(filesize).encode())  #发送文件大小
        has_size = conn.recv(1024).decode()   #接收已下载大小
        print(type(has_size),has_size)
        filenum = 0
        with open(file_path,'rb') as f:
            if has_size != "0":  #断点续传
                f.seek(int(has_size))
            for line in f:   #传送文件
                conn.sendall(line)
                filenum += len(line)
                m.update(line)
                percent = int(100 * filenum / filesize)
                show_str = "[%-100s] %s%%" % (percent * '#', percent)
                print('\r%s' % show_str, file=sys.stdout, flush=True, end='')
        conn.recv(1024) #解决粘包
        conn.sendall(m.hexdigest().encode())
    else:
        print("file does not exist")
        conn.sendall(b'0')  #发送文件大小为0，叫服务器关闭
        return "file does not exist"

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
            to_get(conn,info_dict)
        if info_dict["cmd"] == "put":
            to_put(conn,info_dict)


        re_data = conn.recv(8096).decode()
        print('finally result:',re_data)