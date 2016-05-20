from TagsRecommender.core import tweetsextractor, knn_classification, preprocessor
import json
import threading
import collections


class KnnHashtagsGenerator(threading.Thread):
    def __init__(self, screen_name, current_tweet,
                 number_of_hashtags=4, file_name=""):
        super().__init__()
        self.__screen_name = screen_name
        self.__current_tweet = current_tweet
        self.__number_of_hashtags = number_of_hashtags
        self.__file_name = file_name
        self.recommended_tags = []

    def run(self):
        if self.__file_name == "":
            self.recommended_tags = self.get_recommendations()
        else:
            self.recommended_tags = self.get_recommendations_from_file()

    def get_recommendations(self):
        extractor = tweetsextractor.TweetsExtractor()
        source_tweets = extractor.get_timeline_by_user_screen_name(screen_name=self.__screen_name, size_of_window=200,
                                                                   amount_of_requests=5)
        tweets, current_tweet = self.__process_recommendations(source_tweets)
        knn = knn_classification.KNNClassifier(tweet_words=current_tweet, all_tweets=tweets,
                                                        number_of_hashtags=self.__number_of_hashtags)
        return knn.get_recommended_hashtags()

    def get_recommendations_from_file(self):
        with open(self.__file_name) as data_file:
            source_tweets = json.load(data_file)
        tweets, current_tweet = self.__process_recommendations(source_tweets)
        knn = knn_classification.KNNClassifier(tweet_words=current_tweet, all_tweets=tweets,
                                                        number_of_hashtags=self.__number_of_hashtags)
        return knn.get_recommended_hashtags()

    def __process_recommendations(self, tweets):
        for tweet_index in range(len(tweets)):
            tweets_preprocessor = preprocessor.TweetPreprocessor(tweets[tweet_index])
            tweets[tweet_index] = tweets_preprocessor.tweet
        tweets_preprocessor = preprocessor.TweetPreprocessor(self.__current_tweet)
        preprocessed_tweets = collections.namedtuple('PreprocessedTweets', ['current_tweets', 'previous_tweets'])
        return preprocessed_tweets(tweets, tweets_preprocessor.tweet)
