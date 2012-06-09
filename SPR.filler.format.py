# Script to format filler items for use with linger
#
# Dan Parker June 2012
#
# each line csv file: # FILLER 1 -, This is an example filler item, ? Is this the comprehension question? Y
#
#

import sys, csv

fillers = csv.reader(open(sys.argv[1],"rU"))
output = open('fillers.formatted.txt', 'w')

for row in fillers:
	output.write(row[0] + "\n" + row[1] + "\n" + row[2] + "\n")
	
output.close()
	