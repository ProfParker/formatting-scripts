# Randomizes lines of a text file
# Dan Parker October 2011
#
# Run from terminal

import random

myFile = raw_input("Name of items file (enter full path): ")
myItems = open(myFile)

outputFile = raw_input("Name of output file (enter full path): ")
output = open(outputFile, 'w')

lines = myItems.readlines()
random.shuffle(lines)
for line in lines: 
	output.write(line,)

output.close()