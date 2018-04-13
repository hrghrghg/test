#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
import re
expr='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
expr = expr.replace(' ','')
def calc(string,k):
    k = "([\+\-])*%s([\+\-])*" %k
    parttern = "(\d+\.)?\d+%s(\d+\.)?\d+(%s(\d+\.)?\d+)*" % (k, k)
    lag = False
    print('key:',string)
    while not lag:
        if re.search(parttern,string) is not None:
            r1 = re.search(parttern,string)
            eval1 = eval(r1.group())
            temp = str(eval1)

            string = re.sub(parttern,temp,string,count=1)
            #print(string)
        else:
            lag = True
            print('return-key:',string)
            return string


def parentheses(str1):
    parttern1 = "\([^()]+\)"
    lag = False
    while not lag:
        print('expr:',str1)
        if re.search(parttern1,str1) is not None:
            r1 = re.search(parttern1,str1)
            step1 = r1.group().strip("()")
            step2 = calc(step1,"[\*\/]")
            step3 = calc(step2,'[\+\-]')
            #print('step3:',step3)
            str1 = re.sub(parttern1,step3,str1,count=1)
        else:
            lag = True
            step4 = calc(str1,"[\*\/]")
            step5 = calc(step4, '[\+\-]')
            return step5

# step1 = calc("9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 ","[\*\/]")
# step2 = calc(step1,"[\+\-]")

print(parentheses(expr))

print(eval(expr))

