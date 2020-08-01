import json
import csv

tunefind = {}
with open('rawdata/chartmetricdata/bp_tunefinddata.json') as bp_info:
    data = json.load(bp_info)
    for i in range(len(data['obj'])):
        tunefind_dct = data['obj'][i]
        showdetails = tunefind_dct['show_details']
        tunefind[i] = [tunefind_dct['trackname'], tunefind_dct['showname'], tunefind_dct['showtype'], showdetails[0]['air_date'][:10]]
    

with open('blackpink_tunefind_data.csv', mode='w') as employee_file:
    tunefind_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    tunefind_writer.writerow(['Entry No.', 'Song Name', 'Program Name', 'Program Type', 'Air Date'])

    for num, data in tunefind.items():
        tunefind_writer.writerow([num, data[0], data[1], data[2], data[3]])
