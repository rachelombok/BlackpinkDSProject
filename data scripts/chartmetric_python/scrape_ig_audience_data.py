import json
import csv

ig_countries_dct = {}
ig_cities_dct = {}
ig_gender_per_age = {}
ig_ethnicities = {}
ig_genders ={}
ig_interests = {}
ig_brand_affinities = {}
ig_followers = {}
ig_avg_likes = {}
ig_avg_comments = {}
ig_notable_followers = {}

with open('rawdata/newchartmetricdata/bp_instagram_audience_data.json') as bp_info:
    data = json.load(bp_info)
    for k,v in data['obj'].items():
        if k == 'top_countries':
            for i in range(len(v)):
                ig_countries_dct[v[i]['code']] = [v[i]['name'],v[i]['followers'],v[i]['percent']]

        elif k == 'top_cities':
            for i in range(len(v)):
                ig_cities_dct[v[i]['name']] = [v[i]['followers'], v[i]['percent'], v[i]['country']]
        
        elif k == 'audience_genders_per_age':
            for i in range(len(v)):
                ig_gender_per_age[v[i]['code']] = [v[i]['male'], v[i]['female']]

        elif k == 'audience_ethnicities':
            for i in range(len(v)):
                ig_ethnicities[v[i]['code']] = [v[i]['name'], v[i]['weight']]

        elif k == 'audience_genders':
            for i in range(len(v)):
                ig_genders[v[i]['code']] = [v[i]['weight']]

        elif k == 'audience_brand_affinities':
            for i in range(len(v)):
                ig_brand_affinities[v[i]['name']] = [v[i]['weight']]

        elif k == 'audience_interests':
            for i in range(len(v)):
                ig_interests[v[i]['name']] = [v[i]['weight']]

        elif k == 'followers':
            ig_followers['followers'] = v

        elif k == 'avg_likes_per_post':
            ig_avg_likes['avg_likes_per_post'] = v

        elif k == 'avg_commments_per_post':
            ig_avg_comments['avg_comments_per_post'] = v
            print(v)

        elif k == 'notable_followers':
            for i in range(len(v)):
                ig_notable_followers[v[i]['username']] = [v[i]['picture'], v[i]['followers'], v[i]['url'], v[i]['is_verified']]


with open('bpig_top_countries_data.csv', mode='w') as bpig_top_countries_file:
    bpig_top_countries_writer = csv.writer(bpig_top_countries_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    bpig_top_countries_writer.writerow(['countrycode', 'country', 'followers', 'percent'])

    for code, data in ig_countries_dct.items():
        bpig_top_countries_writer.writerow([code, data[0], data[1], data[2]])


with open('bpig_top_cities_data.csv', mode='w') as bpig_top_cities_file:
    bpig_top_cities_writer = csv.writer(bpig_top_cities_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    bpig_top_cities_writer.writerow(['name', 'followers', 'percent', 'country'])

    for name, data in ig_cities_dct.items():
        bpig_top_cities_writer.writerow([name, data[0], data[1], data[2]])


with open('bpig_gender_per_age_data.csv', mode='w') as bpig_gender_per_age_file:
    bpig_gender_per_age_writer = csv.writer(bpig_gender_per_age_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    bpig_gender_per_age_writer.writerow(['agerange', 'malepercent', 'femalepercent'])

    for code, data in ig_gender_per_age.items():
        bpig_gender_per_age_writer.writerow([code, data[0], data[1]])

with open('bpig_ethnicities_data.csv', mode='w') as bpig_ethnicities_file:
    bpig_ethnicities_writer = csv.writer(bpig_ethnicities_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    bpig_ethnicities_writer.writerow(['code', 'name', 'weight'])

    for code, data in ig_ethnicities.items():
        bpig_ethnicities_writer.writerow([code, data[0], data[1]])

with open('bpig_gender_data.csv', mode='w') as bpig_gender_file:
    bpig_gender_writer = csv.writer(bpig_gender_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    bpig_gender_writer.writerow(['gender', 'percent'])

    for gender, data in ig_genders.items():
        bpig_gender_writer.writerow([gender, data[0]])

with open('bpig_brand_affinities.csv', mode='w') as bpig_brand_affinities_file:
    bpig_brand_affinities_writer = csv.writer(bpig_brand_affinities_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    bpig_brand_affinities_writer.writerow(['name', 'percent'])

    for brand, data in ig_brand_affinities.items():
        bpig_brand_affinities_writer.writerow([brand, data[0]])

with open('bpig_interests.csv', mode='w') as bpig_interests_file:
    bpig_interests_writer = csv.writer(bpig_interests_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    bpig_interests_writer.writerow(['name', 'percent'])

    for interest, data in ig_interests.items():
        bpig_interests_writer.writerow([interest, data[0]])

with open('bpig_numbers_data.csv', mode='w') as bpig_numbers_file:
    bpig_numbers_writer = csv.writer(bpig_numbers_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    bpig_numbers_writer.writerow(['code', 'number'])

    for code, data in ig_followers.items():
        bpig_numbers_writer.writerow([code, data])

    for c, d in ig_avg_likes.items():
        bpig_numbers_writer.writerow([c, d])

    for cd, dt in ig_avg_comments.items():
        bpig_numbers_writer.writerow([cd, dt])



with open('bpig_notable_followers_data.csv', mode='w') as bpig_notable_followers_file:
    bpig_notable_followers_writer = csv.writer(bpig_notable_followers_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    bpig_notable_followers_writer.writerow(['username', 'picture', 'followers', 'link', 'is_verified'])

    for username, data in ig_notable_followers.items():
        bpig_notable_followers_writer.writerow([username, data[0], data[1], data[2], data[3]])





        
