#!/usr/bin/env python
# -*- coding: utf8 -*-
# author aliex-hrg
import logging
from logging import handlers

logger = logging.getLogger('access')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s %(levelname)s')

#sf = logging.FileHandler('test.log',encoding='utf8')
sf = logging.handlers.RotatingFileHandler('test.log',maxBytes=8,backupCount=3,encoding='utf8')
sf.setLevel(logging.ERROR)
sf.setFormatter(formatter)

ss = logging.StreamHandler()
ss.setFormatter(formatter)

logger.addHandler(sf)
logger.addHandler(ss)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')