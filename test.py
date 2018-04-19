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
    def __del__(self):
        print('School del ....')
class Teacher(School):
    def __init__(self,name,age,sex,salary,course):
        School.__init__(self,name,age,sex)
        self.salary = salary
        self.course = course
        self.amount = 3000
    def get_salary(self,amount):
        print('Teacher %s withdraw salary:%s' %(self.name,amount))
        self.amount -= amount
    def __del__(self):
        print('Teacher del ....')
        School.number -= 1
class Student(School):
    def __init__(self,name,age,sex,tuition,course):
        School.__init__(self,name,age,sex)
        self.tuition = tuition
        self.course = course
        self.amount = tuition
    def sign_up(self):
        print("%s student sign up %s,tuition is:%s" %(self.name,self.course,self.tuition))
        self.amount -= self.tuition
t1 = Teacher("lixiang",18,"F",3000,"python")
t2 = Teacher("wuji",12,"M",4000,"linux")
# t3 = Teacher("zhansan",38,"F",30000,"python")
s1 = Student('lihao',10,"F",1000,"python")
# s2 = Student('daguo',12,"M",1200,"java")
print(School.number)
del t2
print(School.number)

# s2.sign_up()
# print(s2.amount)
# print(s1.amount)