import json
import csv

playlist_data = {}
with open('rawdata/chartmetricdata/bp_playlistdata_history.json') as bp_info:
    data = json.load(bp_info)
    for i in range(len(data['obj'])):
        playlist_dct = data['obj'][i]
        timestamp = data['obj'][i]['created_at'][:10]
        playlist_data[timestamp] = [playlist_dct['spotify_ed_playlist_count'],
                            playlist_dct['spotify_playlist_total_reach'],
                            playlist_dct['itunes_ed_playlist_count'],
                            playlist_dct['amazon_ed_playlist_count'],
                            playlist_dct['youtube_ed_playlist_count'],
                            playlist_dct['youtube_playlist_total_reach'],]

with open('blackpink_playlistdata_history.csv', mode='w') as employee_file:
    playlist_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    playlist_writer.writerow(['Date', 
                                'Spotify Editorial Playlist Count', 
                                'Spotify Playlist Total Reach', 
                                'iTunes Editorial Playlist Count',
                                'Amazon Editorial Playlist Count',
                                'Youtube Editorial Playlist Count',
                                'Youtube Playlist Total Reach'])

    for time, info in playlist_data.items():
        playlist_writer.writerow([time, info[0],info[1],info[2],info[3],info[4],info[5]])