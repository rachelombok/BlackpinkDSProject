import spotipy 
import csv
import enchant
import requests
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data

client_id = '0e5d72546dfa4b90b77edac004d9d52c'
client_secret = 'c993f929a18c480090a255dbbc412fa2'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

kamu_uri = 'spotify:track:7jr3iPu4O4bTCVwLMbdU2i'

song_titles = ['ddu-du-ddu-du', 'dont-know-what-to-do', 'kill-this-love', 'boombayah', 'whistle', 'playing-with-fire', 'stay', 'forever-young', 'see-u-later', 'really', 'kick-it', 'hope-not', 'as-if-its-your-last','how-you-like-that']

res = []
for i in range(len(song_titles)):
	r = requests.get('https://genius.com/Genius-english-translations-blackpink-' + song_titles[i] + '-english-translation-lyrics')
	soup = BeautifulSoup(r.text, 'lxml')
	lyrics = soup.find('div', class_='lyrics').get_text()
	res.append([song_titles[i], lyrics])


#kamu = requests.get('')
srcndy = requests.get('https://genius.com/Genius-english-translations-lady-gaga-and-blackpink-sour-candy-english-translation-lyrics')
icecream = requests.get('https://genius.com/Genius-english-translations-blackpink-and-selena-gomez-ice-cream-english-translation-lyrics')
#soup_one = BeautifulSoup(r.text, 'lxml')
soup_two = BeautifulSoup(srcndy.text, 'lxml')
soup_three = BeautifulSoup(icecream.text, 'lxml')
#lyrics_one = soup.find('div', class_='lyrics').get_text()
lyrics_two = soup_two.find('div', class_='lyrics').get_text()
lyrics_three = soup_three.find('div', class_='lyrics').get_text()

res.append(['sour-candy', lyrics_two])
res.append(['ice-cream', lyrics_three])

index = []
lyrics = {}
	
for q in res:
	words = q[1]
	x = words.strip('\n[]:').split()
	index.clear()
	bad =['jennie', 'rosé', 'lisa', 'jisoo','intro', 'chorus', 'pre-chorus', 'verse', 'bridge', 'outro', 'all', '&']
	for j in range(len(x)):
		x[j] =x[j].strip('\n()[]:').lower()
		if any(omit in x[j] for omit in bad):
			x[j] = 'null'
			index.append(j)
			
	var = len(index)
	while var > 0:
		x.remove("null")
		var -= 1

	lyrics[q[0]] = ' '.join(x)
	

with open('blackpink_translated_lyrics.csv', mode='w') as employee_file:
	spotify_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	spotify_writer.writerow(['title', 'lyrics'])
	for key,val in lyrics.items():	
		spotify_writer.writerow([key, val])
