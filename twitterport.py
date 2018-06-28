# QUESTION 4 (ASSIGNMENT 12)
from keys import consumer_key,consumer_secret,access_token,access_secret
import tweepy
oauth=tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api=tweepy.API(oauth)
print(api.search("#dhadak"))
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
user = api.get_user('@BhatnagarSmaily')
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)