#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
import re
expr='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
expr = expr.replace(' ','')
def calc2(expr):
    '''
    传来一个最简单的二元表达式，换算成具体的加减乘除
    :param expr:
    :return:
    '''
    pattern2 = '([\+\-]?\d+(\.\d+)*)'
    r3 = [i for i in re.split(pattern2,expr) if i and i[0] != "."] #此步很关键，切片时带小数的要排除
    if len(r3) == 2:
        symbol = '+'
        num1 = float(r3[0])
        num2 = float(r3[1])
    else:
        symbol = r3[1]
        num1 = float(r3[0])
        num2 = float(r3[2])
    if symbol == '+':
        res = num1 + num2
    elif symbol == '-':
        res = num1 - num2
    elif symbol == '*':
        res = num1 * num2
    else:
        res = num1 / num2
    return res
def calc(string):
    '''
    这是计算不含括号的表达式，先算*/再算+-，从左到右算，最后替换原内容
    :param string: 原表达式最内侧的括号内容
    :return: 返回计算结果
    '''
    parttern1 = '[\+\-]?\d+(\.\d+)*[\*\/][\+\-]?\d+(\.\d+)*' #匹配乘除
    parttern2 = '[\+\-]?\d+(\.\d+)*[\+\-][\+\-]?\d+(\.\d+)*' #匹配加减
    lag = False
    #print('key:',string)
    while not lag:  #计算乘除循环
        if re.search(parttern1,string) is not None:
            r1 = re.search(parttern1,string)
            eval1 = calc2(r1.group())
            if eval1 > 0:   #如果计算结果是负数自然带操作符，是正数得手动赋值加操作符
                temp = '+' + str(eval1)
            else:
                temp = str(eval1)
            string = re.sub(parttern1,temp,string,count=1)
        else:
            while not lag:   #计算加减循环
                if re.search(parttern2,string) is not None:
                    r2 = re.search(parttern2,string)
                    eval2 = calc2(r2.group())
                    if eval2 > 0:
                        temp = '+' + str(eval2)
                    else:
                        temp = str(eval2)
                    string = re.sub(parttern2,temp,string,count=1)
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
            step2 = calc(step1)
            str1 = re.sub(parttern1,step2,str1,count=1)
        else:
            lag = True
            step3 = calc(str1)
            step4 = calc(step3)
            return step4

print('自己算的结果:',parentheses(expr))

print('正解的结果:',eval(expr))

