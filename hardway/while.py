__author__ = 'sereg'

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i +  1
    print "Numbers are :", numbers

print "After while loob, numbers are:"
for num in numbers:
    print num