from __future__ import unicode_literals
from billboard_scrap import get_billboard_list, write_to_file
from ydl import download_list
import sys

if len(sys.argv) == 1:
	print("Downloading Billboards top 100")
	music = get_billboard_list()
	# write_to_file(music)
	download_list(music)
elif len(sys.argv) == 2:
	print("Downloading from url " + sys.argv[1])
	music = get_billboard_list(sys.argv[1])
	download_list(music)
else:
	with open(str(sys.argv[2])) as f:
		lines = [line for line in f.readlines()]
	print("downloading from " + sys.argv[2])
	download_list(lines[:7])