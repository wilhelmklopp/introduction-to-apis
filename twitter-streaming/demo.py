from os.path import join, dirname
from dotenv import load_dotenv
import os

# Taken from: http://adilmoujahid.com/posts/2014/07/twitter-analytics/

# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import requests
import json

# Load environment variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        payload = {
            "text": json.loads(data)["text"],
            "unfurl_links": True,
            "unfurl_media": True
        }
        req = requests.post(os.environ.get("SLACK_HOOK_URL"), json=payload)
        print(req.text)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    # This handles Twitter authetification and the connection to Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # Filter for mentions of copenhacks
    stream.filter(track=['copenhacks'])
