import spotipy 
import csv
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data

client_id = '0e5d72546dfa4b90b77edac004d9d52c'
client_secret = 'c993f929a18c480090a255dbbc412fa2'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

ktltracks = sp.album_tracks('spotify:album:7viSsSKXrDa95CtUcuc1Iv')
sutracks = sp.album_tracks('spotify:album:2zwfcNqJe7IT1RwgVyv1ug')
discography = {}

ktlsongs = ktltracks['items']
while ktltracks['next']:
	ktltracks = sp.next(ktltracks)
	ktlsongs.extend(ktltracks['items'])

susongs = sutracks['items']
while sutracks['next']:
	sutracks = sp.next(sutracks)
	susongs.extend(sutracks['items'])

for song in ktlsongs:
	discography[song['name']] = song
	
for song in susongs:
	discography[song['name']] = song

kamu = sp.track('spotify:track:7jr3iPu4O4bTCVwLMbdU2i')
stay = sp.track('spotify:track:4TWHREp4wv0TmewqR6rgRd')
bbyh = sp.track('spotify:track:3yHQKddM8SVCRnuPSo3HPN')
whstl = sp.track('spotify:track:7HWmJ1wBecOAMNGjC6SmKE')
pwf = sp.track('spotify:track:7e7VjLxO5xJINHvnRytrqi')
aiiyl = sp.track('spotify:track:1Zyd6zQnC6XIIzmg3hP7Ot')

discography[kamu['name']] = kamu
discography[stay['name']] = stay
discography[bbyh['name']] = bbyh
discography[whstl['name']] = whstl
discography[pwf['name']] = pwf
discography[aiiyl['name']] = aiiyl


with open('blackpink_track_data.csv', mode='w') as employee_file:
	spotify_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	# Write csv headers
	spotify_writer.writerow(['Index', 'Artist Name', 'Track Name','Danceability','Energy','Key','Loudness','Speechiness','Accousticness','Instrumentalness','Liveness','Valence','Tempo','Duration MS', 'Release Date'])

	# index
	i = 0
	
	for title,song in discography.items():
		i = i + 1
		
		audio_features = sp.audio_features(song['uri'])[0]
		release_date = sp.track(song['uri'])['album']['release_date']

		# print to console for debugging

		# write to csv

		spotify_writer.writerow([i, 'BLACKPINK', title
					, audio_features['danceability']
					, audio_features['energy']
					, audio_features['key']
					, audio_features['loudness']
					, audio_features['speechiness']
					, audio_features['acousticness']
					, audio_features['instrumentalness']
					, audio_features['liveness']
					, audio_features['valence']
					, audio_features['tempo']
					, audio_features['duration_ms']
					, release_date]
					)





