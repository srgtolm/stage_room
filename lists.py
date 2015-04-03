__author__ = 'sereg'

'''bob = ['Bob Smith', 42, 30000, "software"]
sue = ['Sue Jones', 45, 40000, "hardware"]
#print "name is", bob[0].split()[1]

people = [bob, sue]
def listing(status):
    if status == 1:
        for each in people:
            print(each)
    elif status == 2:
        pays = [pers[2] for pers in people]
        print pays
    elif status == 3:
        print sum(pers[2]for pers in people)

#listing()
tom = ['Tom the man', 15, 27999, "junior"]
people.append(tom)

bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
def field(rec,lab):
    for (fname,fval) in rec:
        if fname == lab:
            return fval
'''
bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')

db = {}
db['bob'] = bob
db['sue'] = sue
#print db
import pprint
#pprint.pprint(db)

'''for key in db:
    print (key, 'is', db[key]['pay'])

for recd in db.values(): print recd['pay']
'''
print -9 / 4