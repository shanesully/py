import sys
import urllib2

if len(sys.argv) != 2:
	print "Usage: python download_page.py [URL]"
	exit()

response = urllib2.urlopen(sys.argv[1])

html = response.read()

name = 'downloaded_page' + '.html'

with open(name, 'w') as f:
	f.write(html)