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

searchlist = []; #hold search list
 #get sepecifc info such as food or any interests
search_info = api.search(q='starbucks',count = 100)    #starbucks related in this case

searchlist.extend(search_info);

for tweet in search_info:
	if 'text' in tweet._json:
 		print(tweet._json['text'])   #print contents

#write objects to json
file = open('tweet.json', 'w') 
print("Writing tweet objects to JSON file")
for status in searchlist:

    json.dump(status._json,file,sort_keys = True,indent = 4)

    
    #close the file
print("Done")
file.close()




print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  ')
#get user timeline, such as starbucks, for latest 100 tweets

tweets = api.user_timeline(id='Starbucks',count=100,tweet_mode="extended")

for t in tweets:

    print(t.full_text)
	

 










