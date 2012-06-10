# Formats experimental items for use with IBEX farm :: Acceptability task
#
# Dan Parker June 2012
#
# Items in txt file, one item per line, no number or whatnot, just the item/sentence
#
# To run :: open terminal, cd to directory with this script, execute 'python ibex-format.py'

import string
import os
import sys

# Prompt for Items file
myFile = raw_input("Name of items file (enter full path): ")
myItems = open(myFile)

# Count the number of lines (i.e. items) from the file
def file_len(fName):
    with open(fName) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

numItems = file_len(myFile)


# Item start number
start = 1

# Prompt for number of conditions 
# (raw_input for text)
conds = int(input("Number of conditions: "))

# Determine number of item sets 
sets = numItems/conds

# Create output file
outputFile = raw_input("Name of output file (enter full path): ")
output = open(outputFile, 'w')

choice =  raw_input("Acceptability or Filler Formatting? enter accept/fill: ")

if choice == "accept":
	for i in range(start,sets+1):
		for x in string.letters[0:conds]:		
			line = myItems.readline()
			item = line[:-1]
			output.write("[[\"" + x + "\", " + repr(i) + "], \"AcceptabilityJudgment\", {s: \"" + item + "\"}],\n")
if choice == "fill":
	for x in range(1,numItems+1):		
		line = myItems.readline()
		item = line[:-1]
		output.write("[\"f" + repr(x) + "\", \"AcceptabilityJudgment\", {s: \"" + item + "\"}],\n")

output.close()



