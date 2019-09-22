# EC601_miniproject1

Hello, this is the miniproject1 of EC601.

In this project, we are going to build a software to analyze twitter contents & images.

Will use twitter API and google natural language API to implement.

Language going to use: Python

- Authors:
- Yufeng Lin     yflin@bu.edu
- Yiming Miao    mym1031@bu.edu




## Google Natural Language API

1.Pre-work

 Before beginning our work, the first thing we have to do is prepareing the environment for Python development. Use command line like:pip install --upgrade google-cloud-storage to insrall some libraries for our project. The most important thing is if you want to run your program in a terminal or something else, you need to set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the file path of the JSON file containing the service account key. This variable only applies to the current shell session. If you open a new shell, you need to set the file path again.
 
 2.Getting setiment from a text
 
 The Python program Google_API_sentiment.py gives an example of analyzing the sentiment of a simple text "Hello, world!". We will get the sentiment score and sentiment magnitude from this API.
