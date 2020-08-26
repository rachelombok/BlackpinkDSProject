import json
import csv

bp_bio = {}
with open('rawdata/chartmetricdata/bp_artistinfodata.json') as bp_info:
    data = json.load(bp_info)
    for k,v in data['obj'].items():
        if k == 'cm_statistics':
            bp_bio['sp_followers'] = v['sp_followers']
            bp_bio['sp_followers_rank'] = v['sp_followers_rank']
            bp_bio['sp_monthly_listeners'] = v['sp_monthly_listeners']
            bp_bio['sp_monthly_listeners_rank'] = v['sp_monthly_listeners_rank']
            bp_bio['ycs_subcribers'] = v['ycs_subscribers']
            bp_bio['ycs_subcribers_rank'] = v['ycs_subscribers_rank']
            bp_bio['ycs_views'] = v['ycs_views']
            bp_bio['ycs_views_rank'] = v['ycs_views_rank']
            bp_bio['tiktok_followers'] = v['tiktok_followers']
            bp_bio['tiktok_followers_rank'] = v['tiktok_followers_rank']
            bp_bio['ins_followers'] = v['ins_followers']
            bp_bio['ins_followers_rank'] = v['ins_followers_rank']
            bp_bio['tiktok_likes'] = v['tiktok_likes']
            bp_bio['tiktok_likes_rank'] = v['tiktok_likes_rank']
            bp_bio['num_sp_editorial_playlists'] = v['num_sp_editorial_playlists']
            bp_bio['sp_playlist_total_reach'] = v['sp_playlist_total_reach']
            bp_bio['num_am_editorial_playlists'] = v['num_am_editorial_playlists']
            bp_bio['num_az_editorial_playlists'] = v['num_az_editorial_playlists']
            bp_bio['num_yt_editorial_playlists'] = v['num_yt_editorial_playlists']
            bp_bio['yt_playlist_total_reach'] = v['yt_playlist_total_reach']
        elif (k in ('name','record_label','band_members','description')):
            bp_bio[k] = v

with open('blackpink_artistinfo_data.csv', mode='w') as employee_file:
    artistinfo_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    artistinfo_writer.writerow(['Label', 'Number'])

    for label, number in bp_bio.items():
        artistinfo_writer.writerow([label, number])
