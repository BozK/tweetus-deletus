import tweepy
import json
import os

# --- MAIN GO BELOW --- #

#Auth
path_to_credentials = os.path.join(os.getcwd(), "creds.json")
with open(path_to_credentials) as file:
    credentials = json.load(file)
auth = tweepy.OAuthHandler(credentials["consumer_key"], credentials["consumer_secret"])
auth.set_access_token(credentials["access_token"], credentials["access_token_secret"])

#Getting ids
with open("condensedTweetIds.json", encoding="utf-8") as f:
    data = json.load(f)

api = tweepy.API(auth)
count = 0
garbage = set()

for tweetId in data:
    print(data[tweetId] + " --- " + str(count))
    try:
        if (data[tweetId]['retweet']):
            api.unretweet(tweetId)
        else:
            api.destroy_status(tweetId)
    except tweepy.error.TweepError:
        garbage.add(tweetId)
        continue
    garbage.add(tweetId)
    count += 1
    if count == 2000:
        break

for i in garbage:
    data.pop(i)

with open("condensedTweetIds.json", encoding="utf-8", mode="w") as f:
    json.dump(data, f)
