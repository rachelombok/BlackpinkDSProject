import json
import csv

from numpy import diff

tt_followers = {}
tt_likes = {}

with open('rawdata/newchartmetricdata/bp_tiktokdata_history.json') as bp_info:
    data = json.load(bp_info)
    for k,v in data['obj'].items():
        if k == 'followers':
            for i in range(len(v)):
                timestamp = v[i]['timestp'][:10]
                total_followers = v[i]['value']
                difference = v[i]['diff']
                if (difference == 'None'):
                    difference = 0

                tt_followers[timestamp] = [total_followers, difference]

        elif k == 'likes':
            for j in range(len(v)):
                timestamp = v[j]['timestp'][:10]
                total_likes = v[j]['value']
                difference = v[j]['diff']
                if (difference == 'None'):
                    difference = 0
              
                tt_likes[timestamp] = [total_likes, difference]

with open('blackpink_tiktokdata_history.csv', mode='w') as newfile:
    tiktok_writer = csv.writer(newfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    tiktok_writer.writerow(['date', 'followers', 'followerdifference', 'likes', 'likesdifference'])

    for date_f, data_f in tt_followers.items():
        
        if (date_f in tt_likes):
            tiktok_writer.writerow([date_f, data_f[0], data_f[1], tt_likes[date_f][0], tt_likes[date_f][1]])
        else:
            tiktok_writer.writerow([date_f, data_f[0], data_f[1], None, None])