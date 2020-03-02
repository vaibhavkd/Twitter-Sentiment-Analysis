import tweepy
import textblob as tb
consumer_key = '6N512kgelH2bKLkcLtAlSAXbE'
consumer_secret = 'GpSauM18nI9GXcAjRMBKwI95b9KWkENRYZNOQAEENS0fNnpBYq'
access_token = '1157742068594368513-xUQLTeJduiPhTMqupSkuuU4L42sJcH'
access_token_secret = '5mbMLETCnNt3zK82jHlDcyRPFnEQ1KTJtc4ZAkDWURfjj'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.search('kobe')
for tweet in public_tweets:
    print(tweet.text)
    analysis = tb.TextBlob(tweet.text)
    print(analysis.sentiment)
