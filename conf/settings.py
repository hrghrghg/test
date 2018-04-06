import sys,os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
    'engine': 'file', #support mysql,postgresql in the future
    'name':'accounts',
    'path': "%s/db" % BASE_DIR
}