#!/usr/bin/env python
# -*- coding: utf8 -*-
# author aliex-hrg
import hashlib
import time
def create_md5():
    m = hashlib.md5()
    m.update(bytes(str(time.time()),encoding='utf8'))
    return m.hexdigest()




print(create_md5())
print(time.time())
