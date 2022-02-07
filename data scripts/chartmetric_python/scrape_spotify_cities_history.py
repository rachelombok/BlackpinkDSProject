import json
import csv
from time import time

spotify_cities = {}

with open('rawdata/newchartmetricdata/bp_spotifycitydata.json') as bp_info:
    data = json.load(bp_info)
    for k,v in data['obj'].items():
        if k == 'cities':
            for key,val in v.items():
                city_dct = {}
                for i in range(len(val)):
                    timestamp = val[i]['timestp'][:10]
                    listeners = val[i]['listeners']
                    rank = val[i]['artist_city_rank']
                    city_dct[timestamp] = [listeners, rank]

                spotify_cities[key] = city_dct

for k,i in spotify_cities.items():
  
    with open('blackpink_spotify_cities_history_' + k[:3] + '.csv', mode='w') as employee_file:
            
        spotify_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        spotify_writer.writerow(['date','listeners','rank'])
        for key,val in i.items():
            spotify_writer.writerow([key, val[0], val[1]])
