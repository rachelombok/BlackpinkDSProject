import json
import csv

from numpy import diff

twt_followers = {}
twt_retweets = {}
last_diff = 0

with open('rawdata/newchartmetricdata/bp_twitterdata_history.json') as bp_info:
    data = json.load(bp_info)
    for k,v in data['obj'].items():
        if k == 'followers':
            for i in range(len(v)):
                timestamp = v[i]['timestp'][:10]
                total_followers = v[i]['value']
                difference = v[i]['diff']
                if (difference == 'None'):
                    difference = 0

                twt_followers[timestamp] = [total_followers, difference]

        elif k == 'retweets':
            for j in range(len(v)):
                timestamp = v[j]['timestp'][:10]
                total_retweets = v[j]['value']
                if (difference == 'None'):
                    difference = 0
                if (j == 0): 
                    last_diff = total_retweets
                    difference = 0
                difference = total_retweets - last_diff
                twt_retweets[timestamp] = [total_retweets, difference]
                last_diff = total_retweets

with open('blackpink_twitterdata_history.csv', mode='w') as newfile:
    twitter_writer = csv.writer(newfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    twitter_writer.writerow(['date', 'followers', 'followerdifference', 'retweets', 'retweetsdifference'])

    for date_f, data_f in twt_followers.items():
        
        if (date_f in twt_retweets):
            twitter_writer.writerow([date_f, data_f[0], data_f[1], twt_retweets[date_f][0], twt_retweets[date_f][1]])
        else:
            twitter_writer.writerow([date_f, data_f[0], data_f[1], None, None])