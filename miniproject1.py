import tweepy
import json
import wget

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

print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

searchlist = []; #hold search list
 #get sepecifc info such as food or any interests, exclude retweets
search_info = api.search(q ='starbucks -filter:retweets',count = 100, include_rts = False, exclude_replies = True)    #starbucks related in this case

searchlist.extend(search_info);

for tweet in search_info:
	if 'text' in tweet._json:
 		print(tweet._json['text'])   #print contents

#write objects to txt
file = open('tweet.txt', 'w') 
print("Writing tweet objects to TXT file")

for tweet in search_info:

	if 'text' in tweet._json:
		print(tweet._json['text'])

		file.write("%s\n" % tweet._json['text'])
    
    #close the file
print("Done")
file.close()


print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
#get user timeline, such as starbucks, for latest 100 tweets
#if user want to search for someone
tweets = api.user_timeline(id='Starbucks',count= 100,tweet_mode="extended")

for t in tweets:

    print(t.full_text)


#download some images
media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])

for media_file in media_files:
    wget.download(media_file)










