'''
@shanesully

Script to change the extension and fix the content of borked
DFXP subtitle translation XML files
'''

import sys

class dfxp_fix(object):
    # DFXP doctor

    def usage_info(self):
        pass

    def __init__(self):
        pass


    def fix_extension(self, file):
        '''
        Change the extension of a given file from whatever it was before
        to plain DFXP
        '''
        
        pass


    def fix_structure(self):
        # Parse and fix missing newlines and broken file structure
        pass

    def debug(self):
        # Display program state
        pass


def main():
    if len(sys.argv) <= 1:
        print "Incorrect usage"
        exit()
    else:
        while sys.argv:
            pass

if __name__ == '__main__':
    main()

