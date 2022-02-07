import spotipy 
import csv
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data

client_id = '0e5d72546dfa4b90b77edac004d9d52c'
client_secret = 'c993f929a18c480090a255dbbc412fa2'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

#other kpop groups
bts = 'spotify:artist:3Nrfpe0tUJi4K4DXYWgMUX'
monstax = 'spotify:artist:4TnGh5PKbSjpYqpIdlW5nz'
redvelvet = 'spotify:artist:1z4g3DjTBBZKhvAroFlhOM'
ateez = 'spotify:artist:68KmkJeZGfwe1OUaivBa2L'
itzy = 'spotify:artist:2KC9Qb60EaY0kW4eH68vr3'
nct127 = 'spotify:artist:7f4ignuCJhLXfZ9giKT7rH'
exo = 'spotify:artist:3cjEqqelV9zb4BYE3qDQ4O'
twice = 'spotify:artist:7n2Ycct7Beij7Dj7meI4X0'

kpop_discography = {}
american_discography = {}
#other american acts

onedirection = 'spotify:artist:4AK6F7OLvEQ5QYCBNiQWHq'
badbunny = 'spotify:artist:4q3ewBCX7sLwd24euuV69X' #ladygaga
brunomars = 'spotify:artist:0du5cEVh5yTK9QJze8zA0C'
theweeknd = 'spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ'
dojacat = 'spotify:artist:5cj0lLjcoR7YOSnhnX0Po5' #katyperry
rihanna = 'spotify:artist:5pKCCKE2ajJHZ9KAiaK11H'
littlemix = 'spotify:artist:3e7awlrlDSwF3iM0WBjGMp'
fifthharmony = 'spotify:artist:1l8Fu6IkuTP0U5QetQJ5Xt'

kpop_artist_list = {'BTS': bts, 'MonstaX': monstax, 'Red Velvet': redvelvet, 'ATEEZ': ateez, 'ITZY': itzy, 'NCT127': nct127, 'EXO': exo, 'Twice': twice}
american_artist_list = {'One Direction': onedirection, 'Bad Bunny': badbunny, 'Bruno Mars': brunomars, 'The Weeknd': theweeknd, 'Doja Cat': dojacat, 'Rihanna': rihanna, 'Little Mix': littlemix, 'Fifth Harmony': fifthharmony}

for name,group in kpop_artist_list.items():
	
	groupalbums = sp.artist_albums(group, None, None, limit = 10, offset = 0)
	
	#get groups' individual albums (limit 10)
	for i in range(len(groupalbums['items'])):
		album_uri = groupalbums['items'][i]['uri']
		album_tracks = sp.album_tracks(album_uri)
		
		#go to their individual tracks
		for j in range(len(album_tracks['items'])):
			album_song = album_tracks['items'][j]
			kpop_discography[album_song['name']] = [name, album_song]
			

with open('kpop_songs_data.csv', mode='w') as employee_file:
	spotify_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	spotify_writer.writerow(['index', 'artist_name', 'track_name','danceability','energy','key','loudness','speechiness','accousticness','instrumentalness','liveness','valence','tempo','duration_ms', 'release_date'])
	
	i = 0
		
	for title,song in kpop_discography.items():
		i = i + 1
	
		audio_features = sp.audio_features(song[1]['uri'])[0]
		release_date = sp.track(song[1]['uri'])['album']['release_date']
		
		spotify_writer.writerow([i, song[0], title
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

for name,artist in american_artist_list.items():
	
	artistalbums = sp.artist_albums(artist, None, None, limit = 20, offset = 0)
	
	#get artists' individual albums
	for i in range(len(artistalbums['items'])):
		album_uri = artistalbums['items'][i]['uri']
		album_tracks = sp.album_tracks(album_uri)
		
		#go to their individual tracks
		for j in range(len(album_tracks['items'])):
			album_song = album_tracks['items'][j]
			
			american_discography[album_song['name']] = [name,album_song]
		
with open('american_songs_data.csv', mode='w') as employee_file:
	spotify_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	spotify_writer.writerow(['index', 'artist_name', 'track_name','danceability','energy','key','loudness','speechiness','accousticness','instrumentalness','liveness','valence','tempo','duration_ms', 'release_date'])
	
	j = 0
		
	for title,song in american_discography.items():
		j = j + 1
	
		audio_features = sp.audio_features(song[1]['uri'])[0]
		release_date = sp.track(song[1]['uri'])['album']['release_date']
		
		spotify_writer.writerow([j, song[0], title
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
