import tweepy

consumer_key = "8kXirmgqZlpt0tJ35MBGfR4aK"
consumer_secret = "mI3RLpJlRrTJwfR6iR9QIxPJPwPo5ZLv7GVVRTH8uDtyKDw4a0"
access_token = "1172954596890697728-izDYLskmhSgZhI5w9XZt6gFBMm1Zem"
access_token_secret = "ZfNgoZp7FFYWHze5JN7DUHbBFmcdOB0Dq5krN6ADoIUKX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


try:
    api.verify_credentials()
    print("Authentication OK")   #verify authentication
except:
    print("Error during authentication")