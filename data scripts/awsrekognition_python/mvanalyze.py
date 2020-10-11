import json
import csv

mvdata = {}

with open('rawdata/mvdata/lsg.json') as bp_info:
    data = json.load(bp_info)
    total = len(data)
    for i in range(len(data)):
        if data[i]['label'] in mvdata:
            mvdata[data[i]['label']] += 1
        else:
            mvdata[data[i]['label']] = 1
            

with open('lsg_mvdata.csv', mode='w') as aiiyl_mvdata_file:
    aiiyl_mvdata_writer = csv.writer(aiiyl_mvdata_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    aiiyl_mvdata_writer.writerow(['Label', 'Frequency'])

    for label, frequency in mvdata.items():
        aiiyl_mvdata_writer.writerow([label, frequency])
