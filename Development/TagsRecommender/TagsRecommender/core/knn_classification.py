import operator
from TagsRecommender.core import additional_functions


class KNNClassifier(object):

    def __init__(self, tweet_words=[], all_tweets=[], number_of_neighbors=10, number_of_hashtags=3):
        self.tweet_words = tweet_words
        self.similar_tweets = additional_functions.similar_tweets(self.tweet_words, all_tweets)
        self.number_of_neighbors = number_of_neighbors
        self.number_of_hashtags = number_of_hashtags

    def get_recommended_hashtags(self):
        neighbors = {}
        for tweet in self.similar_tweets:
            score = 0
            for word in tweet:
                score += self.get_tcor(word)*additional_functions.word_weight(word)
            neighbors[' '.join(tweet)] = score
        nearest_neighbors = []
        # print(neighbors)
        for i in range(self.number_of_neighbors):
            if len(neighbors) == 0:
                break
            curr_max = max(neighbors.items(), key=operator.itemgetter(1))[0]
            nearest_neighbors.append(curr_max)
            neighbors.pop(curr_max)
        # print(nearest_neighbors)
        classifications = {}
        for tweet in nearest_neighbors:
            # print(tweet)
            for hashtag in additional_functions.get_hashtags_of_tweet(tweet.split(' ')):
                if hashtag in classifications:
                    classifications[hashtag] += 1
                else:
                    classifications[hashtag] = 1
        # print(classifications)
        result = []
        for i in range(self.number_of_hashtags):
            if len(classifications) == 0:
                break
            curr_max = max(classifications.items(), key=operator.itemgetter(1))[0]
            result.append(curr_max)
            classifications.pop(curr_max)
        return list(set(result))

    def get_tcor(self, word):
        fl_sum = 0
        fl_count = 0
        tags_with_word = set()
        for tweet in self.similar_tweets:
            if word in tweet:
                fl_sum += len(tweet)
                fl_count += 1
                hashtags = additional_functions.get_hashtags_of_tweet(tweet=tweet)
                for hashtag in hashtags:
                    tags_with_word.add(hashtag)
        fl = fl_sum/fl_count
        cw = len(tags_with_word)
        return ((1/fl if fl != 0 else 0) + (1/cw if cw != 0 else 0))/2




