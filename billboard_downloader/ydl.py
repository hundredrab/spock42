import youtube_dl
import os

ydl_opts = {
	'format': 'bestaudio/best',
	'extractaudio' : True,  # only keep the audio
	'audioformat' : "mp3",  # convert to mp3 
	'outtmpl' : "/home/prophet/Projects/PythonScripts/music_new/%(title)s-%(id)s.mp3",
	'noplaylist' : True,    # only download single song, not playlist
	'quiet' : True, # Don't print anything
	'no_warnings' : True,
}


def download_list(music_list, base = ''):
	""" Takes list of strings as input and donwloads videos into the second-arg base folder. 

	Also adds the list of strings into the downloaded.txt.
	"""

	downloaded = open('downloaded.txt', 'r')
	done_list = [line.strip() for line in downloaded.readlines()]
	downloaded.close()
	new_adds = []
	print("Downloading to " + os.path.join(os.getcwd(), 'music_new'),)
	for song in music_list:
		if str(song).strip() not in done_list:
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				ydl.download(['ytsearch:' + str(song)])
			new_adds.append(song)
			print(song.strip() + ' donwloaded')
			
		else:
			print(song.strip() + ' was donwloaded already.')
	
	with open('downloaded.txt', 'a') as f:
		for new_add in new_adds:
			f.write(new_add.strip() + '\n')
	print(len(new_adds), 'songs downloaded')

