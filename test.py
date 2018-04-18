#!/usr/bin/env python
#!_*_coding:utf8_*_
# author aliex-hrg
import re,os
import sys

class School(object):
    number = 0
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()
    def enroll(self):
        print('%s join school' %self.name)
        School.number += 1
    def info(self):
        print('--------info:',self.name)
        for k,v in self.__dict__.items():
            print(k,v)
        print('--------end')
class Teacher(School):
    def __init__(self,name,age,sex,salary,courge):
        School.__init__(self,name,age,sex)
        self.salary = salary
        self.courge = courge

    def get_salary(self,amount):
        print('Teacher %s withdraw salary:%s' %(self.name,amount))

t1 = Teacher("lixiang",18,"F",3000,"python")
t2 = Teacher("wuji",12,"M",4000,"linux")
t3 = Teacher("zhansan",38,"F",30000,"python")
t1.info()
print(School.number)