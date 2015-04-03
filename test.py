__author__ = 'sereg'

x = 10
y = -11
z = 5.5

#print abs(x),abs(y),abs(z)
#print int(x),int(y),int(z)

def is_int(x):
    if abs(x) - abs(int(x)) > 0:
        print abs(x) - abs(int(x))
        print False
    else:
        print True
#um = raw_input("Num: ")
#print is_int(z)
n = 1986
def digit_sum(n):
    k = 0
    for i in str(n):
        k = k + int(i)
    return k
l = 1
def factorial(n):
    k = 1
    while abs(n) > 0:
        k = k * n
        n = n - 1
    return k

text = "my name is yylis"
k = len(text)

def reverse(text):
    k = len(text) - 1
    z = []
    while k >= 0:
        z.append(text[k])
        k = k - 1
    return ''.join(z)

#print reverse(text)
def anti_vowel(text):
    k = len(text) - 1
    z = []
    for i in text:
        if i == 'y':
            i = ''
        z.append(i)
    print ''.join(z)
#print anti_vowel(text)
word = "python"
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
def scrabble_score(word):
    s = 0
    for i in word:
        s = s + score[i]
        print s
    return s
#print scrabble_score(word)
def censor(text,word):
    z = text.split()
    k = []
    for i in z:
        if i == word:
            i = "*" * len(i)
        k.append(i)

#    print " ".join(k)
#print censor("this hack is wack hack", "hack")
#print censor("hey hey hey","hey")
def count(sequence,item):
    n = 0
    for i in sequence:
        if i == item:
            n +=  1
        print i
    return n
#print count([6, 2, 3, 4, 5, 6],6)
def remove_duplicates(a):
    b = []
    #b.append(a[0])
    for i in a:
            if i not in b:
                b.append(i)
    return b
#print remove_duplicates([4, 5, 5, 4])
def median(m):
    n = sorted(m)
    nn = len(n)
    print "lenght is ", nn
    if nn % 2 == 0:
        k = nn / 2
        zz = (float(n[k]) + float(n[k-1])) / 2
        return zz
    else:
        k = nn / 2
        zz = n[k]
        return zz
#median([5, 2, 3, 1, 4])
print median([5, 2, 3, 1, 4])
print median([5, 2, 3, 1, 4, 6])
#t = 5
#print float(t)/2
#print t / 2
