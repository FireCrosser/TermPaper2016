# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import json

import nltk
import oauth2 as oauth
from pprint import pprint
from twittertags.models import tweet

class TweetsExtractor:

    stopwords = set(nltk.corpus.stopwords.words('english'))

    def __init__(self, consumer_key, consumer_secret):
        self.key = consumer_key
        self.secret = consumer_secret
        self.consumer = oauth.Consumer(key=self.key,
                                       secret=self.secret)
        self.client = oauth.Client(self.consumer)

    def search_all_tweet_by_tag(self, tag="twitter"):
        request_token_url = "https://api.twitter.com/1.1/search/tweets.json?q=%23{tag}&src=typd".format(tag=tag)
        resp, byte_content = self.client.request(request_token_url, "GET")
        content = byte_content.decode("utf-8")
        data = json.loads(content)
        return data
        # pprint(data)

    def get_tweet_by_id(self, tweet_id=0):
        request_token_url = "https://api.twitter.com/1.1/statuses/show.json?id={id}".format(id=tweet_id)
        resp, byte_content = self.client.request(request_token_url, "GET")
        content = byte_content.decode("utf-8")
        data = json.loads(content)
        return data

    def get_timeline_by_user_id(self, user_id=12345):
        request_token_url = "https://api.twitter.com/1.1/statuses/user_timeline.json?" \
                            "user_id={user_id}".format(user_id=user_id)
        resp, byte_content = self.client.request(request_token_url, "GET")
        content = byte_content.decode("utf-8")
        data = json.loads(content)
        return data

    def get_timeline_by_user_screen_name(self, screen_name='fakealexpotter'):
        request_token_url = "https://api.twitter.com/1.1/statuses/user_timeline.json?" \
                            "screen_name={screen_name}".format(screen_name=screen_name)
        resp, byte_content = self.client.request(request_token_url, "GET")
        content = byte_content.decode("utf-8")
        tweets_data = json.loads(content)
        return tweets_data

    @staticmethod
    def __convert_json_to_tweets(json_data):
        pass

    @staticmethod
    def __convert_json_file_to_tweets(json_file):
        pass

    @staticmethod
    def save_to_file(file_name, data):
        with open(file_name, 'w') as outfile:
            json.dump(data, outfile)


if __name__ == "__main__":
    tweets_extractor = TweetsExtractor(consumer_key="1bDsHjtrQ6yWJ7ZQK0Xf2lVfB",
                                        consumer_secret="Ncyt95C3kiSKRQZPZSjURMMe5K7FzV3eirB4fkRQxg0Pe0JgTW")
    # # data = tweets_extractor.search_all_tweet_by_tag("tomhardy")
    # # tweets_extractor.save_to_file("savedtweets.json", data)
    data = tweets_extractor.get_timeline_by_user_screen_name('nike')
    pprint(data)
    # tweets_extractor.save_to_file("json_data/tweetsofuser_byscreenname.json", tweets_extractor)
    # print(data["text"])
