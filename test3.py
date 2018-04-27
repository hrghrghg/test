#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg

import os
a = "get ls"

c,d = a.split()
print(c)
print(d)
print(os.stat('server.py').st_size)