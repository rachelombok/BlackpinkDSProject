import json
import csv

ig_likes = {}
with open('rawdata/newchartmetricdata/bp_instagramdata_history.json') as bp_info:
    data = json.load(bp_info)
    for k,v in data['obj'].items():
        if k == 'followers':
            for i in range(len(v)):
                timestamp = v[i]['timestp'][:10]
                total_followers = v[i]['value']
                difference = v[i]['diff']
                if (difference == 'None'):
                    difference = 0
              
                
                ig_likes[timestamp] = [total_followers, difference]

with open('blackpink_instagramdata_history.csv', mode='w') as employee_file:
    instagram_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    instagram_writer.writerow(['date', 'followers', 'difference'])

    for time, likes in ig_likes.items():
        instagram_writer.writerow([time, likes[0], likes[1]])
