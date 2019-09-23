import tweepy
import json

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


try:
    api.verify_credentials()
    print("Authentication OK")   #verify authentication
except:
    print("Error during authentication")


 #get sepecifc info such as food or any interests

 search_info = api.search(q='starbucks',count = 100)    #starbucks related in this case

 for tweet in search_info:

 	if 'text' in tweet._json:
 		print(tweet._json['text'])   #print contents

 		output_file.write(json.dumps(tweet._json))  


 #get user timeline, such as starbucks

 for alltweets in tweepy.Cursor(api.user.timeline,screen_name ='@Starbucks Coffee',tweet_mode = "extended").items():

 	print(alltweets.full_text)

 










