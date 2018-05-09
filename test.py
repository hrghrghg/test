#!/usr/bin/env python
#!_*_coding:utf8_*_
# author aliex-hrg
import re,os
import sys

# !/usr/bin/python3.6
# __*__uft8__*__
import sys,os,optparse
import time,threading


class argv(object):
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option("-s","--server",dest="host",help="bind to server address")
        parser.add_option("-p","--port",dest="port",help="bind to server port")
        (options,args) = parser.parse_args()
        print(options,args)
        print(options.host,options.port)
        print(args[1])