#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
import sys,os,time,re




c = "D:\\ftp\\.\\.\\..\\12\\13\\.."
print(re.sub('(\\\\\.)+\\\\\.\.','\\..',c,count=1))
#print(re.sub('\\\\\.[^\.]','',c))
print(c)