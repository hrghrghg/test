#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
import re
expr='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
expr = expr.replace(' ','')
def calc(string,k):
    '''
    这是一元或二元计算不含括号，从左到右算，最后替换原内容
    :param string: 原表达式最内侧的括号内容
    :param k: 为一元只算加减，二元只算*/
    :return: 返回计算结果
    '''
    k = "([\+\-])*%s([\+\-])*" %k   #加减*/前后可能有多个加减
    parttern = "[\*\/\+\-]*(\d+\.)?\d+%s(\d+\.)?\d+(%s(\d+\.)?\d+)*" % (k, k)  #匹配类似内容-12.0102+-2.432+12
    lag = False
    #print('key:',string)
    while not lag:
        if re.search(parttern,string) is not None:
            r1 = re.search(parttern,string)
            eval1 = eval(r1.group())
            temp = '+' + str(eval1)
            string = re.sub(parttern,temp,string,count=1)
            #print(string)
        else:
            lag = True
            #print('return-key:',string)
            return string.strip('+')

def parentheses(str1):
    '''
    这是依次取出最内侧括号函数，交给calc计算，返回再替换原内容
    :param str1:
    :return:
    '''
    parttern1 = "\([^()]+\)"   #匹配最内侧括号
    lag = False
    while not lag:
        #print('expr:',str1)
        if re.search(parttern1,str1) is not None:
            r1 = re.search(parttern1,str1)
            step1 = r1.group().strip("()")
            step2 = calc(step1,"[\*\/]")
            step3 = calc(step2,'[\+\-]')
            str1 = re.sub(parttern1,step3,str1,count=1)
        else:
            lag = True
            step4 = calc(str1,"[\*\/]")
            step5 = calc(step4, '[\+\-]')
            return step5

print('自己算的结果:',parentheses(expr))

print('正解的结果:',eval(expr))

