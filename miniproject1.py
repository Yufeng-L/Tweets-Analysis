from google.cloud import language_v1
from google.cloud.language_v1 import enums
import google.api_core.exceptions
import six
import tweepy
import json
import wget
import matplotlib.pyplot as plt
import wordcloud
import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import collections

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")  # verify authentication
except:
    print("Error during authentication")

print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

user_input = input("please enter your keyword : ");

searchlist = [];  # hold search list
# get sepecifc info such as food or any interests, exclude retweets
search_info = api.search(q=user_input + '-filter:retweets', count=100, include_rts=False,
                         exclude_replies=True)  # starbucks related in this case

searchlist.extend(search_info);

for tweet in search_info:
    if 'text' in tweet._json:
        print(tweet._json['text'])  # print contents

# write objects to txt
file = open('tweet.txt', 'w')
print("Writing tweet objects to TXT file")

for tweet in search_info:

    if 'text' in tweet._json:
        print(tweet._json['text'])

        file.write("%s\n" % tweet._json['text'])

# close the file
print("Done")
file.close()

print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n')

client = language_v1.LanguageServiceClient()

with open('/Users/linyufeng/Desktop/EC601_miniproject1/tweet.txt', 'r') as f:
    content = f.read().splitlines()
    # print(content)
    # length = len(content)
    # print(length)
# content = ' Hello, world!'
# f = open('/Users/mym/Desktop/test.txt')
# content = f.read()
f.close()


if isinstance(content, six.binary_type):
    content = content.decode('utf-8')

type_ = enums.Document.Type.PLAIN_TEXT
a = []
b = []
pos1 = []
neg1 = []
pos2 = []
neg2 = []

c = 0.0
d = 0.0
for s in content:
    try:
        document = {'type': type_, 'content': s}
        response = client.analyze_sentiment(document)
        sentiment = response.document_sentiment
        a.append(sentiment.score)
        b.append(sentiment.magnitude)
        if sentiment.score >= 0:
            pos1.append(sentiment.score)
        if sentiment.score < 0:
            neg1.append(sentiment.score)
        if sentiment.score >= 0:
            pos2.append(sentiment.magnitude)
        if sentiment.score >= 0:
            neg2.append(sentiment.magnitude)
        c += sentiment.score
        d += sentiment.magnitude
        # print('Score: {}'.format(sentiment.score))
        # print('Magnitude: {}'.format(sentiment.magnitude))
    except google.api_core.exceptions.InvalidArgument:
        pass
n = len(a)
m = len(b)
p = len(pos1)
q = len(neg1)
# count1 = 0
# count2 = 0
# count3 = 0
# count4 = 0
if 0 <= c/n <= 0.15:
    print('In general, People have lightly positive attitude towards' + ' ' + user_input)
elif c/n >= 0.15:
    print('In general, People have clearly positive attitude towards' + ' ' + user_input)
elif -0.15 <= c/n < 0:
    print('In general, People have lightly negative attitude towards' + ' ' + user_input)
else:
    print('In general, People have clearly negative attitude towards' + ' ' + user_input)

print('There are ' + 'percent: {:.2%}'.format(p/(q+p)) + 'people have positive attitude towards' + ' ' + user_input)
print('There are ' + 'percent: {:.2%}'.format(q/(q+p)) + 'people have negative attitude towards' + ' ' + user_input)


print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n')

#generate word cloud to visualize text
fn = open('tweet.txt','r',encoding = 'utf-8')
text = fn.read()

text = " ".join(jieba.cut(text))

fn.close()
stopwords = set(STOPWORDS)
stopwords.update(["https", "fuck", "fucking"])
wc = WordCloud( background_color = 'white',  
                max_words = 200,            
                max_font_size = 60,          
                color_func = None,            
                random_state = 42,  
                stopwords = stopwords         
                ).generate(text)

plt.imshow(wc,interpolation = "bilinear")
plt.axis('off')
plt.show()

wc.to_file('/Users/linyufeng/Desktop/EC601_miniproject1/cloud.png')


