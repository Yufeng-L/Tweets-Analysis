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

- 1.Pre-work

 Before beginning our work, the first thing we have to do is prepareing the environment for Python development. Use command line like:pip install --upgrade google-cloud-storage to insrall some libraries for our project. The most important thing is if you want to run your program in a terminal or something else, you need to set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the file path of the JSON file containing the service account key. This variable only applies to the current shell session. If you open a new shell, you need to set the file path again.
 
- 2.Getting sentiment from a text
 
 The Python program Google_text_sentiment.py gives an example of analyzing the sentiment of a simple text "Hello, world!". We will get the sentiment score and sentiment magnitude from this API.
 
- 3.Getting entity's sentiment from a text

 The python program Google_entity_sentiment.py gives an example of getting entities from a text and analyze their sentiment score and sentiment magnitude.
 
## Here is the architecture of our APP:

![Architecutre: ](https://github.com/Yufeng-L/EC601_miniproject1/blob/master/architecture.png)

## Here is the Sample Visualizatoin of Result (Key word: 'Starbucks')
![SampleWordcloud: ](https://github.com/Yufeng-L/EC601_miniproject1/blob/master/cloud.png)

## Here is the Sample Output of Sentiment Anlaysis (Key word: 'Starbucks')

![SampleOutput_Sentiment: ](https://github.com/Yufeng-L/EC601_miniproject1/blob/master/sampleoutput.png)

