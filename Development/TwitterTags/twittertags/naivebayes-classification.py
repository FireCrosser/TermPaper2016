
class BayesClassificator(object):

    def __init__(self, tweet_words, all_tweets, number_of_hashtags=3):
        self.tweet_words = tweet_words
        self.all_tweets = all_tweets
        self.number_of_hashtags = number_of_hashtags

