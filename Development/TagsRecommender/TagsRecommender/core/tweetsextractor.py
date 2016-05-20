# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import json

import nltk
import oauth2 as oauth
from pprint import pprint


class TweetsExtractor:
    stopwords = set(nltk.corpus.stopwords.words('english'))

    def __init__(self, consumer_key="1bDsHjtrQ6yWJ7ZQK0Xf2lVfB",
                 consumer_secret="Ncyt95C3kiSKRQZPZSjURMMe5K7FzV3eirB4fkRQxg0Pe0JgTW"):
        self.key = consumer_key
        self.secret = consumer_secret
        self.consumer = oauth.Consumer(key=self.key,
                                       secret=self.secret)
        self.client = oauth.Client(self.consumer)

    def search_all_tweet_by_tag(self, tag="twitter"):
        request_token_url = "https://api.twitter.com/1.1/search/tweets.json?q=%23{tag}&src=typd".format(tag=tag)
        resp, byte_content = self.client.request(request_token_url, "GET")
        content = byte_content.decode("ac")
        data = json.loads(content)
        return data
        # pprint(data)

    def get_timeline_by_user_id(self, user_id=12345):
        request_token_url = "https://api.twitter.com/1.1/statuses/user_timeline.json?" \
                            "user_id={user_id}".format(user_id=user_id)
        resp, byte_content = self.client.request(request_token_url, "GET")
        content = byte_content.decode()
        data = json.loads(content)
        return data

    def get_timeline_by_user_screen_name(self, screen_name='NBA', size_of_window=300, amount_of_requests=15):
        max_id = 0
        result_tweets = []
        for i in range(amount_of_requests):
            if i == 0:
                request_token_url = "https://api.twitter.com/1.1/statuses/user_timeline.json?" \
                                    "screen_name={screen_name}&count={count}" \
                    .format(screen_name=screen_name, count=size_of_window)
            else:
                max_id += size_of_window
                request_token_url = "https://api.twitter.com/1.1/statuses/user_timeline.json?" \
                                    "screen_name={screen_name}&count={count}&max_id={max_id}" \
                    .format(screen_name=screen_name, count=size_of_window, max_id=max_id)
            resp, byte_content = self.client.request(request_token_url, "GET")
            content = byte_content.decode("utf-8")
            tweets_data = json.loads(content)
            result_tweets += [(tweet['id'], tweet['text']) for tweet in tweets_data]
            max_id = result_tweets[-1][0]
        return [entry[1] for entry in result_tweets]

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
    data = tweets_extractor.get_timeline_by_user_screen_name('TheAcademy', 100, 10)
    tweets_extractor.save_to_file('json_data/users_tweets.json', data)
