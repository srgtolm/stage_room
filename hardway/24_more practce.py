__author__ = 'sereg'

print "Lets Practice everything"

poem = """la - la
lp - la
xu - i - ta"""

print "-----------------------"
print poem
print "-----------------------"

five = 10 - 2 - 7  - 1 + 5
print "The five is: %d" % five

def secret_formula(five):
    jelly = five + 2
    jars = jelly * 2
    crates = jelly + jars
    return  jelly, jars,crates

print "-----------------------"
print "Jelly is: %d Jars is : %d Crates is : %d" % (secret_formula(five))