#! /usr/local/bin/python
# 
# shanesully
#
# Extract strings from given xml files
#

import sys
from BeautifulSoup import BeautifulStoneSoup


def print_usage():
    print "\nUsage:\n\n\t$ python {} $OPTIONS $XML_FILES".format(sys.argv[0])
    print "\nOptions:\n"
    print "\t-k: Create language dictionary\n"
    print "\t-s: Create .txt file of strings\n"


def create_strings_file(files):
    '''
    Create a file of newline-terminated strings based on string
    attribute tags for every given xml file
    '''
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


def create_language_dict(files):
    '''
    Return a dict of string attribs and combined values from every given xml file
    '''
    strings = {}

    for given_file in files:
        with open(given_file) as xml_source_file:
            soup = BeautifulStoneSoup(xml_source_file)

            for tag in soup.findAll(['string', 'plurals']):

                if str(tag['name']) in strings:
                    strings[str(tag['name'])].append(tag.text.encode('utf-8'))
                else:
                    strings[str(tag['name'])] = [ tag.text.encode('utf-8') ]

    return strings


def main():
    if sys.argv[1] == '-s':
        create_strings_file(sys.argv[2:])
    elif sys.argv[1] == '-k':
        create_language_dict(sys.argv[2:])
    else:
       print_usage() 


if __name__ == '__main__':

    if len(sys.argv) <= 1:
        print_usage()
        sys.exit()

    main()
