__author__ = 'sereg'

from os.path import exists

script = "copy-scrimp.py"
from_file = "first.txt"
to_tile = "second.txt"

print "Copying from %s to %s" % (from_file, to_tile)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)
print "Does the output file exists? %r" % exists(to_tile)
print "Press any key"
raw_input(">")

out_file = open(to_tile, "w")
#out_file.truncate()
out_file.write(indata)

print "Copying ....Done."

out_file.close()
in_file.close()