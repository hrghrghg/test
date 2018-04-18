import sys,os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
    'engine': 'file', #support mysql,postgresql in the future
    'name':'accounts',
    'path': "%s/db" % BASE_DIR
}

TANSACTION_TYPE = {
    'withdraw':{'action':'minus','interest':0.05},
    'repay':{'action':'plus','interest':0},
    'transfer':{'action':'minus','interest':0.05}
}