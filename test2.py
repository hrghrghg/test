#!/usr/bin/env python
# -*- coding: utf8 -*-
# author aliex-hrg
import re

a = "-1388337.0476190478--1.2"
k = "[\+\-]"
#k = "([\+\-])*%s" % k
aparttern = "\ ?(\d+\.)?\d+\ ?%s\ ?(\d+\.)?\d+(\ ?%s\ ?(\d+\.)?\d+)*" % (k, k)
parttern = "^[\+\-]\d+\.\d+"
r1 = re.search(parttern,a)


print(r1.group())