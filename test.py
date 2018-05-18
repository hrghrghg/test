#!/usr/bin/env python
#!_*_coding:utf8_*_
# author aliex-hrg
import configparser

cnf = configparser.ConfigParser()
cnf.read("C:\\Users\\Administrator\\Desktop\GitHub\\test\作业\\简单批量主机管理\\conf\\host.ini")

print(cnf.sections())