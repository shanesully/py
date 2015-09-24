# shanesully
# File extensions changer

import os
import sys


def print_usage_info():
    print "$ python {} $args $new_extension".format(sys.argv[0])


def sanitize_extension(extension):
    # Check for missing period
    if extension[0] != '.':
        return '.' + extension


def change_extension(files, new_extension):
    for a_file in files:
        # Strip old extension
        base = os.path.splitext(a_file)[0]
        # Rename file in filesystem
        os.rename(a_file, base + new_extension)


def main():

    if len(sys.argv) <= 1:
        print_usage_info()
        exit()

    # New extension is the final arg - Validate styling
    new_extension = sanitize_extension(sys.argv.pop())

    # Update extension for all files
    change_extension([ a_file for a_file in sys.argv[1:] ], new_extension)

    
if __name__ == '__main__':
    main()

