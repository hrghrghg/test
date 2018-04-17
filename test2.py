#!/usr/bin/env python
# -*- coding: utf8 -*-
# author aliex-hrg
import re

#expr='-1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
expr = '-10.23243/-3.432'
pattern1 = '([\+\-]?\d+(\.\d+)*)'
l = [i for i in re.split('([\+\-]?\d+(\.\d+)?)',expr) if i and i[0] != "."]
print(l)
