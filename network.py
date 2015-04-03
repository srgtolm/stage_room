__author__ = 'sereg'

from sys import argv

script = "network.py"
#filename = "ex15_sample1.txt"
filename = raw_input("print file name> ")

raw_input("?")

print "Opening file:"
target = open(filename, "w")

print "Truncating the file. Goodway!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I'm going to write these lines to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

target.close()


#file_again = raw_input("> ")
#txt_again = open(file_again, "w")
#txt_again.write("SOME XXX")
#print txt_again.read()