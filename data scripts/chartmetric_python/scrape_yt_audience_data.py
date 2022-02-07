import json
import csv

yt_countries_dct = {}
yt_gender_per_age = {}
yt_genders ={}
yt_subscribers = {}
yt_avg_likes = {}
yt_avg_comments = {}
yt_notable_subscribers = {}

with open('rawdata/newchartmetricdata/bp_youtube_audience_data.json') as bp_info:
    data = json.load(bp_info)
    for k,v in data['obj'].items():
        if k == 'top_countries':
            for i in range(len(v)):
                #print(v)
                yt_countries_dct[v[i]['code']] = [v[i]['name'],v[i]['subscribers'],v[i]['percent']]

        elif k == 'audience_genders_per_age':
            for i in range(len(v)):
                yt_gender_per_age[v[i]['code']] = [v[i]['male'], v[i]['female']]

        elif k == 'audience_genders':
            for i in range(len(v)):
                yt_genders[v[i]['code']] = [v[i]['weight']]

        elif k == 'subscribers':
            yt_subscribers['subscribers'] = v

        elif k == 'avg_likes_per_post':
            yt_avg_likes['avg_likes_per_post'] = v

        elif k == 'avg_commments_per_post':
            yt_avg_comments['avg_comments_per_post'] = v

        elif k == 'notable_subscribers':
            for i in range(len(v)):
                yt_notable_subscribers[v[i]['fullname']] = [v[i]['picture'], v[i]['subscribers'], v[i]['url'], v[i]['is_verified']]


with open('bpyt_top_countries_data.csv', mode='w') as bpyt_top_countries_file:
    bpyt_top_countries_writer = csv.writer(bpyt_top_countries_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    bpyt_top_countries_writer.writerow(['country_code', 'country', 'subscribers', 'percent'])

    for code, data in yt_countries_dct.items():
        bpyt_top_countries_writer.writerow([code, data[0], data[1], data[2]])


with open('bpyt_gender_per_age_data.csv', mode='w') as bpyt_gender_per_age_file:
    bpyt_gender_per_age_writer = csv.writer(bpyt_gender_per_age_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    bpyt_gender_per_age_writer.writerow(['agerange', 'male_percent', 'female_percent'])

    for code, data in yt_gender_per_age.items():
        bpyt_gender_per_age_writer.writerow([code, data[0], data[1]])

with open('bpyt_gender_data.csv', mode='w') as bpyt_gender_file:
    bpyt_gender_writer = csv.writer(bpyt_gender_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    bpyt_gender_writer.writerow(['gender', 'percent'])

    for gender, data in yt_genders.items():
        bpyt_gender_writer.writerow([gender, data[0]])

with open('bpyt_numbers_data.csv', mode='w') as bpyt_numbers_file:
    bpyt_numbers_writer = csv.writer(bpyt_numbers_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    bpyt_numbers_writer.writerow(['code', 'number'])

    for code, data in yt_subscribers.items():
        bpyt_numbers_writer.writerow([code, data])

    for c, d in yt_avg_likes.items():
        bpyt_numbers_writer.writerow([c, d])

    for cd, dt in yt_avg_comments.items():
        bpyt_numbers_writer.writerow([cd, dt])



with open('bpyt_notable_followers_data.csv', mode='w') as bpyt_notable_followers_file:
    bpyt_notable_followers_writer = csv.writer(bpyt_notable_followers_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    bpyt_notable_followers_writer.writerow(['fullname', 'picture', 'subscribers', 'link', 'is_verified'])

    for username, data in yt_notable_subscribers.items():
        bpyt_notable_followers_writer.writerow([username, data[0], data[1], data[2], data[3]])



