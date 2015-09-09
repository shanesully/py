#! /usr/local/bin/python
# 
# shanesully
#
# Extract strings from an xml file
#
import sys
from BeautifulSoup import BeautifulStoneSoup

if len(sys.argv) == 1:
    print "Incorrect arguments\n\nUsage:\n\t$ python extract_strings.py arg1"
    sys.exit()

# XML strings file
src = open(sys.argv[1])
# Strip src file extension and append
dest_name = str(sys.argv[1][:-4]) + "_strings" + ".txt"
dest = open(dest_name, 'w+')

soup = BeautifulStoneSoup(src)

words = []

for tag in soup.findAll(['string', 'plurals']):
   words.append(tag.text.encode('utf-8'))

# Populate names file
for word in words:
    dest.write(word + '\n')

print "Word count: {}".format(len(words))
print "{} file created".format(dest_name)
