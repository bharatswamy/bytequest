import tweepy
from django.conf import settings

# Add your Twitter API credentials
consumer_key = settings.CONSUMER_KEY
consumer_secret = settings.CONSUMER_SECRET
access_token = settings.ACCESS_TOKEN
access_token_secret = settings.ACCESS_TOKEN_SECRET

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create the API object
api = tweepy.API(auth)

# Fetch your tweets
username = settings.TWITTER_USERNAME  # Replace with your Twitter username
tweets = api.user_timeline(
    screen_name=username, count=10
)  # Change count to fetch more tweets if needed

# Display the tweets
for tweet in tweets:
    print(tweet.text)
    print("---")
