import json
import csv

sp_follower_data = {}
sp_listener_data = {}
sp_ftl_data = {}
with open('rawdata/chartmetricdata/bp_spotifydata_history.json') as bp_info:
    data = json.load(bp_info)
    for k,v in data['obj'].items():
        if k == 'followers':
            #print('f',len(v))
            for i in range(len(v)):
                follower_data_dct = v[i]
                timestamp = follower_data_dct['timestp'][:10]
                sp_follower_data[timestamp] = [follower_data_dct['value'], follower_data_dct['diff']]

        elif k == 'listeners':
            #print('l',len(v))
            for j in range(len(v)):
                listener_data_dct = v[j]
                timestamp = listener_data_dct['timestp'][:10]
                sp_listener_data[timestamp] = [listener_data_dct['value'], listener_data_dct['diff']]

        elif k == 'followers_to_listeners_ratio':
            #print('ftl',len(v))
            for m in range(len(v)):
                ftl_data_dct = v[m]
                timestamp = ftl_data_dct['timestp'][:10]
                sp_ftl_data[timestamp] = [ftl_data_dct['value'], ftl_data_dct['diff']]

#print("follow ", sp_follower_data)
#print("listener ", sp_listener_data)

count = 0
with open('blackpink_spotifydata_combinedtwo.csv', mode='w') as newfile:
    sp_combined_writer = csv.writer(newfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    sp_combined_writer.writerow(['date', 'followers', 'followerdifference', 'monthlylisteners', 'monthlylistenersdifference'])

    for date_f, data_f in sp_follower_data.items():
        if (date_f in sp_listener_data):
            sp_combined_writer.writerow([date_f, data_f[0], data_f[1], sp_listener_data[date_f][0], sp_listener_data[date_f][1]])
        else:
            sp_combined_writer.writerow([date_f, data_f[0], data_f[1], None, None])


"""

with open('blackpink_spotifydata_followers_history.csv', mode='w') as emp_file:
    sp_follower_writer = csv.writer(emp_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    sp_follower_writer.writerow(['Date', 'Followers', 'Follower Difference'])

    for date, data in sp_follower_data.items():
        sp_follower_writer.writerow([date, data[0],data[1]])
                

with open('blackpink_spotifydata_listeners_history.csv', mode='w') as employee_file:
    sp_listener_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    sp_listener_writer.writerow(['Date', 'Monthly Listeners', 'Monthly Listeners Difference'])

    for date, data in sp_listener_data.items():
        sp_listener_writer.writerow([date, data[0],data[1]])

with open('blackpink_spotifydata_ftl_history.csv', mode='w') as e_file:
    sp_ftl_writer = csv.writer(e_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    sp_ftl_writer.writerow(['Date', 'Followers to Listeners Ratio','Followers to Listeners Ratio Difference'])

    for date, data in sp_ftl_data.items():
        sp_ftl_writer.writerow([date, data[0],data[1]])
"""