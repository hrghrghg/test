#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
import time

print(time.time())

print(time.mktime(time.strptime("2014-1-1",'%Y-%m-%d')))
while True:
    a = input().strip()
    print(a.isdecimal())
    print(float(a))