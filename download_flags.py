#!/usr/bin/python

import sys
import urllib2
from bs4 import BeautifulSoup


gallery_url = 'https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags'
if len(sys.argv) > 1 and sys.argv[1]:
	gallery_url = sys.argv[1]

try:
	source = BeautifulSoup(urllib2.urlopen(gallery_url).read())
except:
	print('Error with URL {}.'.format(gallery_url))
	print('You may want to try the default URL.')
	quit()

for img in source.find_all('img'):
	src = img.get('src')

	if not 'Flag_of' in src:
		continue

	src = 'http:'+src.replace('thumb/', '')
	src = '/'.join(src.split('/')[0:-1])

	print(src)

	flag_image = urllib2.urlopen(src).read()
	with open(src.split('/')[-1], 'wb') as out:
		out.write(flag_image)
