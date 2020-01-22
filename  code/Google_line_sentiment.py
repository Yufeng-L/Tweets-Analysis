from google.cloud import language_v1
from google.cloud.language_v1 import enums
import google.api_core.exceptions
import six

client = language_v1.LanguageServiceClient()

with open('/Users/mym/Documents/python/Google/tweet.txt', 'r') as f:
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
    print('In general, People have lightly positive attitude towards' + ' ' + 'user_input')
elif c/n >= 0.15:
    print('In general, People have clearly positive attitude towards' + ' ' + 'user_input')
elif -0.15 <= c/n < 0:
    print('In general, People have lightly negative attitude towards' + ' ' + 'user_input')
else:
    print('In general, People have clearly negative attitude towards' + ' ' + 'user_input')

print('There are ' + 'percent: {:.2%}'.format(p/(q+p)) + 'people have positive attitude towards' + ' ' + 'user_input')
print('There are ' + 'percent: {:.2%}'.format(q/(q+p)) + 'people have negative attitude towards' + ' ' + 'user_input')