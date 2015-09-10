#! /usr/local/bin/python
# 
# shanesully
#
# Extract strings from an xml file

import sys
from BeautifulSoup import BeautifulStoneSoup

if len(sys.argv) <= 1:
    print "Incorrect arguments\n\nUsage:\n\n\t$ python {} example.xml ...\n".format(sys.argv[0])
    sys.exit()

for given_file in sys.argv[1:]:

    file_format = str(given_file).split('.')[1] 

    if file_format == 'xml':

        with open(given_file) as xml_source_file:
            strings_file_name = str(xml_source_file.name).split('.')[0] + "_strings.txt"

            with open(strings_file_name, 'w+') as strings_file:
                soup = BeautifulStoneSoup(xml_source_file)
                strings = []

                for tag in soup.findAll(['string', 'plurals']):
                   strings.append(tag.text.encode('utf-8'))

                for string in strings:
                    strings_file.write(string + '\n')

                print "String count: {}".format(len(strings))
                print "{} file created".format(strings_file_name)
    else:
        print "Ignoring {} as it is .{} format and not .xml".format(given_file, str(given_file).split('.')[1])
