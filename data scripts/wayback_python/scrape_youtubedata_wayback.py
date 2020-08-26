import os
import sys
import requests as rq
from bs4 import BeautifulSoup as bs
from time import sleep
from time import time
from random import randint
#from warnings import warn
import json
import pandas as pd
import scrapy
import codecs
import re
import csv
'''
#renaming all snapshot homepage files, only needed to be run once
directory = os.fsencode('/Users/rachelombok/Downloads/BPspotify/youtubescrape/youtube.com/channel/UCOmHUn--16B90oW2L6FRR3A')
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".snapshot"): 
        base = os.path.splitext(filename)[0]
        os.rename('/Users/rachelombok/Downloads/BPspotify/youtubescrape/youtube.com/channel/UCOmHUn--16B90oW2L6FRR3A/' + filename, '/Users/rachelombok/Downloads/BPspotify/youtubescrape/youtube.com/channel/UCOmHUn--16B90oW2L6FRR3A/' + base + '.txt')
        print(filename)
'''
str_dir = '/Users/rachelombok/Downloads/BPspotify/youtubescrape/youtube.com/channel/UCOmHUn--16B90oW2L6FRR3A'
directory = os.fsencode(str_dir)
numbers = ['1','2','3','4','5','6','7','8','9','0']
stats_dct = {}
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    datedfile = open(str_dir + '/' + filename, 'r', encoding= 'utf-8', errors= 'replace')
    for line in datedfile:
        line.encode('utf-8').strip()
        index = line.find('subscribers')
        if (index != -1) and (filename.endswith(".txt")):
            rawsubs = line[index:index+23]
            subnumber = rawsubs.strip('subscribers"></span>')
            for num in numbers:
                if num in subnumber:
                    if 'M' in subnumber:
                        x = subnumber.strip('M')
                        if '.' in x:
                            sublst = x.split('.')
                            subnumber = sublst[0] + ',' + sublst[1] + '00,000'
                        else:
                            subnumber = x + ',000,000'
                    subdate = filename[:8]
                    stats_dct[subdate] = subnumber
                    break

with open('youtube_scrape_data.csv', mode='w') as employee_file:
    youtube_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    youtube_writer.writerow(['Date', 'Subscribers'])
    i = 0

    for date,subs in stats_dct.items():
        i += 1
        youtube_writer.writerow([date,subs])
	
		

		





	