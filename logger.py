#!_*_coding:utf-8_*_
#__author__:"Alex huang"
import logging
#logging.basicConfig(filename='test.log',level=logging.ERROR,format='%(asctime)s %(filename)s:%(lineno)d %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)
formater=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# fl = logging.FileHandler('access.log',encoding='utf8')
# fl.setLevel(logging.WARN)
# fl.setFormatter(formater)
#
# cl = logging.StreamHandler()
# cl.setLevel(logging.ERROR)
# cl.setFormatter(formater)
#
# logger.addHandler(cl)
# logger.addHandler(fl)

logger.info('fdsafdsafd')
logger.debug('fdsafdsafd')
logger.warning('fdsafdsafd')
logger.error('fdsafdsafd')
logger.critical('fdsafdsafd')
