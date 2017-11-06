import requests, bs4

def get_billboard_list(url = None):
	if url == None:
		url = "http://www.billboard.com/charts/hot-100" # The url of list
	elif url in ['pop', 'country', 'rock', 'indie']:
		url = "http://www.billboard.com/charts/" + url + "songs"
	print("Downloading page")
	res = requests.get(url, "lxml")
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, "lxml")
	song_rows = soup.select('.chart-row__container')
	music = []
	for song in song_rows:
		song_tup = tuple([song.select('h2')[0].getText().strip(), song.select('.chart-row__artist')[0].getText().strip()])
		music.append(song_tup[1] + ' - ' + song_tup[0])
	print(music)
	return music

def write_to_file(music):
	f = open('music_list.txt', 'w')
	for song in music:
		f.write(song[1] + ' - ' + song[0] + '\n')
	f.close()

if __name__ == '__main__':
	music = get_billboard_list()
	print('Getting list')
	write_to_file(music)
	print('Done!')
