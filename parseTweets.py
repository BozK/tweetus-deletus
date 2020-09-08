import json
from datetime import datetime

YEARS_OF_NOTE = ["2012", "2013", "2014", "2015"]

def parseDate(iter):
    return data[iter]['tweet']['created_at'].split(" ")[-1]

def isRetweet(iter):
    return data[iter]['tweet']['full_text'][:2] == 'RT'

def getId(iter):
    return data[iter]['tweet']['id']


#MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN
with open("tweet.json", encoding="utf-8") as f:
    data = json.load(f)

output = {}

for i in range(len(data)):
    if (thisDate := parseDate(i)) in YEARS_OF_NOTE:
        output[getId(i)] = {'retweet': isRetweet(i), 'year': thisDate}

with open("condensedTweetIds.json", "w") as f:
    json.dump(output, f)
    

