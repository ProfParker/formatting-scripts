# This script takes SPR items in excel files and formats the items for use with linger
#
# Original source unknown. DP June 2012
#
# Instructions:
# 1. Save each condition to a separate csv file.
# 2. Execute: python SPR_process_items.py condA.csv condB.csv condC.sv questions.csv > formattedItems.txt

#!/usr/bin/python

import sys,codecs,string

def split_quotes(s, sep=',', quote='"', escape='\\'):
  NORMAL = 0
  INSIDE_QUOTE = 1
  ESCAPED_NORMAL = 2
  ESCAPED_QUOTE = 3
  v = []
  state = NORMAL
  curr = u''
  for c in s:
    if (state == NORMAL):
      if (c == quote):
        state = INSIDE_QUOTE
      elif (c == escape):
        state = ESCAPED_NORMAL
      elif (c == sep):
        v.append(curr)
        curr = u''
      else:
        curr += c
    elif (state == INSIDE_QUOTE):
      if (c == quote):
        state = NORMAL
      elif (c == escape):
        state = ESCAPED_QUOTE
      else:
        curr += c
    elif (state == ESCAPED_NORMAL):
      curr += c
      state = NORMAL
    elif (state == ESCAPED_QUOTE):
      curr += c
      state = QUOTE
  v.append(curr)
  return v

def tag(items, tags):
  if not (len(items) == len(tags)):
    sys.stderr.write(items + '\n')
    sys.stderr.write(len(items) + '\n')
    sys.stderr.write(tags + '\n')
    sys.stderr.write(len(tags) + '\n')
  assert len(items) == len(tags)
  tagged_items = []
  for i in range(len(items)):
    if items[i] != '':
      tagged_items.append(items[i] + tags[i])
  return tagged_items

  
# main

#The command line arguments (except the last) are the item file names
item_fns = sys.argv[1:(len(sys.argv)-1)]
# The last command line argument is the question file name
ques_fn = sys.argv[(len(sys.argv)-1)]

# Read question file
ques_fo = codecs.open(ques_fn, "r", "latin1")
qs = []
for l in ques_fo.readlines():
  n,q = split_quotes(l.strip())
  qs.append(string.replace(q, "\"", ""))
ques_fo.close()

# Read item files
labls = []
items = []
i = 1
for item_fn in item_fns:
  item_fo = codecs.open(item_fn, "r", "latin1")
  lines = item_fo.readlines()
  hdr = lines[0]
  tags = [si.strip("\"") for si in split_quotes(hdr.strip())[1:len(hdr)]]
  labls_cf = []
  items_cf = []
  for l in lines[1:len(lines)]:
    s = split_quotes(l.strip())
    label_c = s[0] 
    items_c = tag([si.strip() for si in s[1:len(s)]], tags)
    labls_cf.append(label_c)
    items_cf.append(items_c)
  labls.append(labls_cf)
  items.append(items_cf)
  sys.stderr.write("... done item file " + str(i) + '\n')
  i += 1

# Check input
if not (len(labls) == len(items)):
  sys.stderr.write("Length of labls was " + str(len(labls)) + '\n')
  sys.stderr.write("Length of items was " + str(len(items)) + '\n')
assert len(labls) == len(items)
for labls_cf in labls:
  if not (len(qs) == len(labls_cf)):
    sys.stderr.write("Length of qs was " + str(len(qs)) + '\n')
    sys.stderr.write("Length of labls_cf was " + str(len(labls_cf)) + '\n')
  assert len(qs) == len(labls_cf)
for items_cf in items:
  if not (len(qs) == len(items_cf)):
    sys.stderr.write("Length of qs was " + str(len(qs)) + '\n')
    sys.stderr.write("Length of labls_cf was " + str(len(items_cf)) + '\n')
  assert len(qs) == len(items_cf)

# Output
for i_f in range(len(labls)):
  labls_cf = labls[i_f]
  items_cf = items[i_f]
  for i_l in range(len(labls_cf)):
    print labls_cf[i_l].encode("latin1")
    print ' '.join(items_cf[i_l]).encode("latin1")
    print qs[i_l].encode("latin1")
