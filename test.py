#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author aliex-hrg
import hmac

m = hmac.new(b'aaaa',b'fdsafd')

print(m.hexdigest())
