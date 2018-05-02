#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
import sys,os,time
c = "k"
m = {}
m["s"] = 1
m["b"] = 2
m[c] = 3
width = 50
percent = 1
show_str=('[%%-%ds]' %width) %(int(width*percent) * '#')
print('\r%s %d%%' %(show_str,int(100*percent)),file=sys.stdout,flush=True,end='')

show_str = "[%-100s]" %(int(percent)*'#')
print(show_str)