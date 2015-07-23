#! /usr/local/bin/python
#
# Wed 22 Jul 2015 11:49:30 IST
# 
# sos
#
# Creates a csv file of name attribs
# based on a given strings.xml file
#
import sys
from BeautifulSoup import BeautifulStoneSoup

if len(sys.argv) == 1:
    print "Incorrect arguments\n\nUsage:\n\t$ python soup.py arg1"
    sys.exit()

# XML file with string tags
src = open(sys.argv[1])
# Strip src file extension and append
dest_name = str(sys.argv[1][:-4]) + "_names" + ".csv"
dest = open(dest_name, 'w')

soup = BeautifulStoneSoup(src)

# Create list of string names
words = []

for tag in soup.findAll(['string', 'plurals']):
   words.append(tag['name'])

# Create file of string names
for word in words:
    dest.write(word + ',\n')
