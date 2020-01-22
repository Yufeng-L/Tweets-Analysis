# :sparkles: Tweets Analysis :sparkles:

Hello, this is the miniproject1 of EC601.

In this project, we are going to build a software to help user analyze their desired food/products. The user can enter a keyword and then the software will tell the user about the attitude towards the keyword in Twitter. What's more, the software will output a word cloud based on the input keyword.

We will use Twitter API and Google natural language API to implement.

Language: Python

- Authors:
- __Yufeng Lin     yflin@bu.edu__
- __Yiming Miao    mym1031@bu.edu__

## Tweepy API:
Bascially we use tweepy to get the most recent 100 tweets based on user's desired input.
Also, user can serach for someone's recent tweets. (Deleted in the latest ver)
This app will mainly focused on tweepy's serach module.

## Scenario of this app:
User A wants to know comments about the specific product such as Starbucks, and they can get related tweets contain the key word "Starbucks". For the latest implementation, we ask users to enter their desired keyword, and then the program can search for latest 100 tweets. Then we use Google Natrual Language API to analyze those tweets to get positive/nagative feedbacks based on those texts. 
### :warning: Reminder: Don't forget to include '' when entering key word :warning:
## User Stories
- I, the user, should be able to grab most recent tweets with my desired input.
- I, the user, should be able to grab tweets through one's timeline. __(Deleted in the latest ver)__
- I, the user, should be able to visualize the results of output. __(Via wordcloud)__
- I, the user, should be able to get sentiment analysis from Google Natural Language API about my desired input.

## Steps for installing

    (1)Download the python program __miniproject1.py__.
    (2)Pip the packages that you don't have.
    (3)Set the path of tweet.txt.
    (4)Set the path of world cloud picture where you want to save.
    (5)Set the Twitter key.
    (6)Run this program in a terminal, the first command line is: export GOOGLE_APPLICATION_CREDENTIALS="your json key location". Then you can run our program.

## Google Natural Language API

- __Pre-work__

 Before beginning our work, the first thing we have to do is prepareing the environment for Python development. Use command line like:__pip install --upgrade google-cloud-storage__ to install some libraries for our project. The most important thing is if you want to run your program in a terminal or something else, you need to set the environment variable __GOOGLE_APPLICATION_CREDENTIALS__ to the file path of the JSON file containing the service account key. This variable only applies to the current shell session. If you open a new shell, you need to set the file path again.
 
- __Get sentiment from a text__
 
 The Python program __Google_text_sentiment.py__ gives an example of analyzing the sentiment of a simple text "Hello, world!". We will get the sentiment score and sentiment magnitude from this API.

- __Get entities from a text__

 The Python program Google_keyword.py gives an example of getting keywords(or in other words:the entities) from the text. Entities can be broadly divided into two categories: proper nouns or common nouns (also called "nouns" in natural language processing) that correspond to unique entities (specific characters, places, etc.). If something is a noun, it will be recognized as an entity.
 
- __Get entity's sentiment from a text__

 The Python program __Google_entity_sentiment.py__ gives an example of getting entities from a text and analyze their sentiment score and sentiment magnitude.
 
- __Get every line's sentiment from a text__

 The Python program __Google_line_sentiment.py__ gives an example of analysing the text's attitude line by line. This program can give you both the whole attitude and the percentage of people who have the positive attitude and the percentage of people who have the negative attitude. This program is finally used in our project in __miniproject1.py__
 
- __Problems Encountered__

 (1) At first, we tried to get the entity(keyword) from the text to analyze its sentiment. However, the entities capture was not accurate as we have assumed. For most of times, the program can't catch the entities accurately, which means that the program will catch lots of meaningless words. Even if the keyword was in the list of entities capture, it was not a pure entity or in other words, it would contain a long sentence. 
 
 (2) We have to find another way to analyze the text. Since we got the tweets from Twitter API with text, we did some research with the format of the tweets we have caught. Every line in the text profile of tweets is one person's tweet. Therefore, we can read the text line by line and analyze line by line with Google_text_sentiment.py.
 
 (3) The Google natural language API will return two parameters of the analysis result. One is score, the other is magnitude. Score of the sentiment ranges between -1.0 (negative) and 1.0 (positive) and corresponds to the overall emotional leaning of the text. Magnitude indicates the overall strength of emotion (both positive and negative) within the given text, between 0.0 and +inf. Unlike score, magnitude is not normalized; each expression of emotion within the text (both positive and negative) contributes to the text's magnitude (so longer text blocks may have greater magnitudes).
 
 (4) From the tweets we have caught from Twitter API, we can find that most of the tweets are short. It would be too hard to caculate the sentiment with both of the two parameters since we are going to estimate the whole attitude towards the keyword. Therefore, we finally decided to use score as our parameter to measure the sentiment.
 
## Here is the architecture of our APP:

![Architecutre: ](https://github.com/Yufeng-L/EC601_miniproject1/blob/master/architecture.png)

## Here is the Sample Visualizatoin of Result (Key word: 'Starbucks')
![SampleWordcloud: ](https://github.com/Yufeng-L/Tweets-Analysis/blob/master/%20output/cloud.png)

## Here is the Sample Output of Sentiment Anlaysis (Key word: 'Starbucks')

![SampleOutput_Sentiment: ](https://github.com/Yufeng-L/Tweets-Analysis/blob/master/%20output/sampleoutput.png)

