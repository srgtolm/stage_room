from __future__ import print_function
__author__ = 'sereg'

from storeload import loadDbase
db = loadDbase()
#for key in db:
#    print(key, '=>\n', db[key])
import pprint
pprint.pprint(db)


'''
from storeload import loadDbase,storeDbase
db = loadDbase()
print(db)
db['sue']['pay'] = 49999
db['bob']['name'] = 'Bob Smith Jr.'
print(db)
storeDbase(db)

'''