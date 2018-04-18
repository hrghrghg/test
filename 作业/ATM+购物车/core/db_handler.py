#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
from conf import settings

def db_handler(conn_parms):
    if conn_parms['engine'] == "file":
        return file_db_handler(conn_parms)
    if conn_parms['engine'] == "mysql":
        return mysql_db_handler(conn_parms)

def mysql_db_handler(parm):
    pass

def file_db_handler(parm):
    db_path = "%s/%s" %(parm['path'],parm['name'])
    return db_path

print(db_handler(settings.DATABASE))