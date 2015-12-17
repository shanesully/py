# Merge xml translation files

from sys import argv
import re

if len(argv) != 3:
	exit("\nIncorrect num args\n\tRequires: $INPUT_FILE.xml $INPUT_STRINGS.txt\n")

with open(argv[1]) as f:
	xml_file = f.read().splitlines()

with open(argv[2]) as f:
	strings_file = f.read().splitlines()

exp = re.compile(r">.*?<")

with open(str(argv[1]) + ".new", "w+") as output_file:
	for line, string in zip(xml_file, strings_file):
		line = re.sub(exp, ">" + string + "<", line)
		output_file.write(line + "\n")

