#!_*_coding:utf-8_*_
#__author__:"Alex huang"
import logging,time
from logging import handlers

#logging.basicConfig(filename='test.log',level=logging.ERROR,format='%(asctime)s %(filename)s:%(lineno)d %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)
formater=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formater1=logging.Formatter('%(asctime)s  %(levelname)s %(message)s')

#fl = logging.FileHandler('access.log',encoding='utf8')
fl = logging.handlers.TimedRotatingFileHandler('access.log',when='S',interval=5,backupCount=4,encoding='utf8')
fl.setLevel(logging.DEBUG)
fl.setFormatter(formater)

cl = logging.StreamHandler()
cl.setLevel(logging.ERROR)
cl.setFormatter(formater1)

logger.addHandler(cl)
logger.addHandler(fl)

logger.debug('fdsafdsafd你')
logger.info('fdsafdsaf授信d')
logger.warning('fdsafd热武器 safd')
logger.error('fdsafd热武器 safd')
logger.critical('fdsa热武器 fdsafd')
