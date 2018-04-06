#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
def a(type):
    print(type)
    def b(func):
        print(func)
        def c(*args,**kwargs):
            print("\033[34;1mfdasfdasf\033[0m")
            func(args[0])
        return c
    return b
@a("parm a")
def x(a):
    print("in the b",a)

x("Fdsfd")