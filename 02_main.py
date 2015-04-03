__author__ = 'sereg'

n = [3, 5, 7]

def total(numbers):
    print numbers
    result = 0
    for i in range(len(numbers)):
        result = result + numbers[i]
#       print "Num" + str(i)
    print numbers[i]
    return result
#print total(n)
#print range(len(n))


"""for k in n:
    print k
result = 0
for item in range(len(n)):
    result = result + n[item]
    #print n[i]
    print result """

n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for item in range(len(words)):
        result = result + words[item]
        print words[item]
    return result


print join_strings(n)
"""print n[0]
print n[1]
k = ""
k = n[0]
k = k + n[1]
print k"""