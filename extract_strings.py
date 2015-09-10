#! /usr/local/bin/python
# 
# shanesully
#
# Extract strings from an xml file

import sys
from BeautifulSoup import BeautifulStoneSoup

if len(sys.argv) <= 1:
    print "\n\nUsage:\n\n\t$ python {} example.xml ...\n".format(sys.argv[0])
    sys.exit()

def create_basic_strings_file(files):
    """
    Creates a new file of newline-terminated strings based on the strings
    attribute tags for every given xml file
    """
    for given_file in files:
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

                    print "{} file created with {} strings".format(strings_file_name, len(strings))
        else:
            print "Ignoring {} as it is in .{} format and not .xml".format(given_file, str(given_file).split('.')[1])

def main():
    if sys.argv[1] == '-s':
        create_basic_strings_file(sys.argv[2:])

if __name__ == '__main__':
    main()
