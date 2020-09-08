# tweetus-deletus

Usage:
- Request tweet archive
- Extract zip, pull out "tweets.js"
    - Clean it up a bit to be friendly with python json package
- In parseTweets: specify what years' tweets to be extracted
- Run parseTweets, generating condensedTweetIds.json
    - This file has key-value pairs of tweetIds: {year, retweet status}
- Fill out creds.json with twitter api keys
- Run tweetusDeletus; by default this runs up to 2000 times. Adjust if you wish (or just set it to a huge number)

Notes:
this code may be a mess, but it's *my mess* :)
