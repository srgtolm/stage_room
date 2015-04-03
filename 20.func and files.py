__author__ = 'sereg'

from sys import argv

script = "func.py"
input_file = "first.txt"

def read_file(f):
    print f.read()

def find_line(f):
    f.seek(0)

def print_a_line(line_count, f):

    print line_count, f.readline(),

curr_file = open(input_file)
print "Firdt lets print whole file:"
read_file(curr_file)
print "Second let's rewind, kind of like a tape."
find_line(curr_file)
print "Third let's print three lines"
curr_line = 1
print_a_line(curr_line, curr_file)
curr_line += 1
print_a_line(curr_line, curr_file)
curr_line += 1
print_a_line(curr_line, curr_file)
print "New"

#from grab import Grab
#import logging
#logging.basicConfig(level=logging.DEBUG)
#g = Grab()
#g.go("python.org")
#print g.xpath('//a[@class="reference external"]').get('href')

