import json
import csv

fb_likes = {}
with open('rawdata/chartmetricdata/bp_facebookdata_history.json') as bp_info:
    data = json.load(bp_info)
    for k,v in data['obj'].items():
        if k == 'likes':
            for i in range(len(v)):
                timestamp = v[i]['timestp'][:10]
                total_likes = v[i]['value']
                difference = v[i]['diff']
                if (difference == 'None'):
                    difference = 0
                
                #print(v[i]['timestp'][:10])
                fb_likes[timestamp] = [total_likes, difference]

        #print(k, type(v))

with open('blackpink_facebook_data_history.csv', mode='w') as employee_file:
    facebook_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    facebook_writer.writerow(['Date', 'Likes', 'Difference'])

    for time, likes in fb_likes.items():
        facebook_writer.writerow([time, likes[0], likes[1]])