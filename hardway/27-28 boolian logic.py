__author__ = 'sereg'

db = []

def inputf():
    db = []
    a = raw_input("PrintOne> ")
    if a == "stop":
        print "break"
        exit()
    db.append(a)
    b = raw_input("PrintTwo> ")
    db.append(b)
    m = raw_input("What to do> ")
    db.append(m)
    return  printer(db)

def false_true(n):
    if n == "True":
        return True
    elif n == "False":
        return False
    elif n == "not False":
        return True
    elif n == "not True":
        return False
    else:
        return n

def printer(db):
    for i in range(len(db)):
        if db[i] == "stop":
            print "break"
            break
    if db[2] == "and":
         print db[0] + " and " + db[1]
         print false_true(db[0]) and false_true(db[1])
         inputf()
    elif db[2] == "or":
         print db[0] + " or " + db[1]
         print false_true(db[0]) or false_true(db[1])
         inputf()





inputf()
