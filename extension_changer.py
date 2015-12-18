# Change file extensions

import os
import sys


def print_usage_info():
    # Commandline usage info
    print("\nUsage:\n")
    print("\t$ python {} $files $new_extension\n".format(sys.argv[0]))
    print("Notes:\n")
    print("\t- $files can be any number of individual files or a directory")
    print("\t- $new_extension can omit a period\n")


def sanitize_extension(extension):
    # Check for missing period
    if extension[0] != '.':
        return '.' + extension


def change_extension(files, new_extension):
    # Change the extension of files provided to the new extension
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

