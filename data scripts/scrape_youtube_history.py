import json
import csv

yt_subscriber_history = {}
yt_views_history = {}
yt_videos_history = {}

with open('rawdata/chartmetricdata/bp_youtubechanneldata_history.json') as bp_info:
    data = json.load(bp_info)
    for k,v in data['obj'].items():
        if k == 'subscribers':
            for i in range(len(v)):
                sub_dct = v[i]
                subtimestamp = sub_dct['timestp'][:10]
                yt_subscriber_history[subtimestamp] = [sub_dct['value'], sub_dct['diff']]
        
        elif k == 'views':
            for j in range(len(v)):
                view_dct = v[j]
                viewtimestamp = view_dct['timestp'][:10]
                yt_views_history[viewtimestamp] = [view_dct['value'], view_dct['diff']]

        elif k == 'videos':
            for m in range(len(v)):
                vid_dct = v[m]
                vidtimestamp = vid_dct['timestp'][:10]
                yt_videos_history[vidtimestamp] = [vid_dct['value'], vid_dct['diff']]

with open('blackpink_youtube_subscriber_history.csv', mode='w') as employee_file:
    sub_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    sub_writer.writerow(['Date', 'Subscribers', 'Difference'])

    for time, subs in yt_subscriber_history.items():
        sub_writer.writerow([time, subs[0], subs[1]])

with open('blackpink_youtube_views_history.csv', mode='w') as emp_file:
    views_writer = csv.writer(emp_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    views_writer.writerow(['Date', 'Views', 'Difference'])

    for time, views in yt_views_history.items():
        views_writer.writerow([time, views[0], views[1]])

with open('blackpink_youtube_videos_history.csv', mode='w') as e_file:
    vid_writer = csv.writer(e_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    vid_writer.writerow(['Date', 'Videos', 'Difference'])

    for time, vid in yt_videos_history.items():
        vid_writer.writerow([time, vid[0], vid[1]])
