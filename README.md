# EC601 Miniproject1

Hello, this is the miniproject1 of EC601.

In this project, we are going to build a software to help user analyze their desired food/products. The user can enter a keyword and then the software will tell the user about the attitude towards the keyword in Twitter. What's more, the software will also give user a world cloud based on the input keyword.

We will use Twitter API and Google natural language API to implement.

Language: Python

- Authors:
- Yufeng Lin     yflin@bu.edu
- Yiming Miao    mym1031@bu.edu

## Tweepy API:
Bascially we use tweepy to get the most recent 100 tweets based on user's desired input.
Also, user can serach for someone's recent tweets. (Deleted in the latest ver)
This app will mainly focused on tweepy's serach module.

## Scenario of this app:
User A wants to know comments about the specific product such as Starbucks, and they can get related tweets contain the key word "Starbucks". For the latest implementation, we ask users to enter their desired keyword, and then the program can search for latest 100 tweets. Then we use Google Natrual Language API to analyze those tweets to get positive/nagative feedbacks based on those texts. 
### Reminder: don't forget to add '' when entering key word
## User Stories
- I, the user, should be able to grab most recent tweets with my desired input.
- I, the user, should be able to grab tweets through one's timeline. (Deleted in the latest ver)
- I, the user, should be able to visualize the results of output. (Via wordcloud)
- I, the user, should be able to get sentiment analysis from Google Natural Language API about my desired input.

## Google Natural Language API

- __Pre-work__

 Before beginning our work, the first thing we have to do is prepareing the environment for Python development. Use command line like:pip install --upgrade google-cloud-storage to insrall some libraries for our project. The most important thing is if you want to run your program in a terminal or something else, you need to set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the file path of the JSON file containing the service account key. This variable only applies to the current shell session. If you open a new shell, you need to set the file path again.
 
- __Get sentiment from a text__
 
 The Python program Google_text_sentiment.py gives an example of analyzing the sentiment of a simple text "Hello, world!". We will get the sentiment score and sentiment magnitude from this API.

- __Get entities from a text__

 The Python program Google_keyword.py gives an example of getting keywords(or in other words:the entities) from the text. Entities can be broadly divided into two categories: proper nouns or common nouns (also called "nouns" in natural language processing) that correspond to unique entities (specific characters, places, etc.). If something is a noun, it will be recognized as an entity.
 
- __Get entity's sentiment from a text__

 The Python program Google_entity_sentiment.py gives an example of getting entities from a text and analyze their sentiment score and sentiment magnitude.
 
- __Problems Encountered__

 (1) At first, we tried to get the entity(keyword) from the text to analyze its sentiment. However, the entities capture was not accurate as we have assumed. For most of times, the program can't catch the entities accurately, which means that the program will catch lots of meaningless words. Even if the keyword was in the list of entities capture, it was not a pure entity or in other words, it would contain a long sentence. 
 
 (2) We have to find another way to analyze the text. Since we got the tweets from Twitter API with text, we did some research with the format of the tweets we have caught. Every line in the text profile of tweets is one person's tweet. Therefore, we can read the text line by line and analyze line by line with Google_text_sentiment.py.
 
 (3) The Google natural language API will return two parameters of the analysis result. One is score, the other is magnitude. Score of the sentiment ranges between -1.0 (negative) and 1.0 (positive) and corresponds to the overall emotional leaning of the text. Magnitude indicates the overall strength of emotion (both positive and negative) within the given text, between 0.0 and +inf. Unlike score, magnitude is not normalized; each expression of emotion within the text (both positive and negative) contributes to the text's magnitude (so longer text blocks may have greater magnitudes).
 
 (4) From the tweets we have caught from Twitter API, we can find that most of the tweets are short. It would be too hard to caculate the sentiment with both of the two parameters since we are going to estimate the whole attitude towards the keyword. Therefore, we finally decided to use score as our parameter to measure the sentiment.
 
## Here is the architecture of our APP:

![Architecutre: ](https://github.com/Yufeng-L/EC601_miniproject1/blob/master/architecture.png)

## Here is the Sample Visualizatoin of Result (Key word: 'Starbucks')
![SampleWordcloud: ](https://github.com/Yufeng-L/EC601_miniproject1/blob/master/cloud.png)

## Here is the Sample Output of Sentiment Anlaysis (Key word: 'Starbucks')

![SampleOutput_Sentiment: ](https://github.com/Yufeng-L/EC601_miniproject1/blob/master/sampleoutput.png)

