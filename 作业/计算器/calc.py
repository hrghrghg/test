#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
import re
expr='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

def calc(string,k):
    parttern = "(\d+\.)?\d+\ ?\%s\ ?\d+(\.\d+)?" %k
    k = "\%s" %k
    lag = False
    while not lag:
        if re.search(k,string) is not None:
            r1 = re.search(parttern,string)
            eval1 = eval(r1.group())
            print('eval:',eval1)
            if eval1 < 0.00000001 and eval1 > 0:
                temp = "0"
                print("遇到小数位太多的了")
            else:
                temp = str(eval(r1.group()))
            string = re.sub(parttern,temp,string,count=1)
            print(string)
        else:
            lag = True
            return string

step1 = calc('9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 ',"*")
step2 = calc(step1,"/")
step3 = calc(step2,"+")
step4 = calc(step3,"-")
print(step4)
print(eval('9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 '))



# exit_flag = False
# sum = 0
# while not exit_flag:
#     if re.search('\([^\(\)]+\)',expr) is not None:
#         temp = re.search('\([^\(\)]+\)',expr).group().strip('()')
#         print('temp:',temp)
#         eva = str(eval(temp))
#         print(eva)
#         expr = re.sub('\([^\(\)]+\)',eva,expr)
#         print(expr)
#     else:
#         exit_flag = True

