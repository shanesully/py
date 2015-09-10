#! /usr/local/bin/python
# 
# shanesully
#
# Extract strings from an xml file

import sys
from BeautifulSoup import BeautifulStoneSoup

if len(sys.argv) != 2:
    print "Incorrect arguments\n\nUsage:\n\n\t$ python {} example.xml\n".format(sys.argv[0])
    sys.exit()

with open(sys.argv[1]) as xml_file:
    file_name = str(xml_file.name).split('.')[0] + "_strings.txt"

    with open(file_name, 'w+') as strings_file:
        soup = BeautifulStoneSoup(xml_file)
        strings = []

        for tag in soup.findAll(['string', 'plurals']):
           strings.append(tag.text.encode('utf-8'))

        for string in strings:
            strings_file.write(string + '\n')

        print "String count: {}".format(len(strings))
        print "{} file created".format(file_name)
