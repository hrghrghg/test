#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
import time,pickle,uuid,hashlib

def create_md5():
    m = hashlib.md5()
    m.update(bytes(str(time.time()), encoding='utf8'))
    return m.hexdigest()

def create_uuid():
    return str(uuid.uuid1())

if __name__ == '__main__':
    print(create_uuid())
    print(create_md5())