import json
import csv


with open('rawdata/chartmetricdata/bp_spotifycitydata.json') as bp_info:
    data = json.load(bp_info)
    for k,v in data['obj'].items():
        pass