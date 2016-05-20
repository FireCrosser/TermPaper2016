import operator

from TagsRecommender.core import additional_functions


class BayesClassificator(object):

    def __init__(self, tweet_words=[], all_tweets=[], number_of_hashtags=4):
        self.tweet_words = tweet_words
        self.similar_tweets = additional_functions.similar_tweets(self.tweet_words, all_tweets)
        self.number_of_hashtags = number_of_hashtags
        self.all_haghtags = self.__get_all_hashtags()

    def get_recommended_hashtags(self):
        classifications = {}
        result = []
        for hashtag in self.all_haghtags:
            score = 0
            hashtag_prob = self.__hashtag_probability(hashtag)
            for word in self.tweet_words:
                score += (self.__cond_probability(word, hashtag)*hashtag_prob)*additional_functions.word_weight(word)
            classifications[hashtag] = score
        for n in range(self.number_of_hashtags):
            if len(classifications) == 0:
                break
            curr_max = max(classifications.items(), key=operator.itemgetter(1))[0]
            result.append(curr_max)
            classifications.pop(curr_max)
        return result

    def __cond_probability(self, word, hashtag):
        # amount of tweets where word and hashtag occur together
        prob_count = 0
        for tweet in self.similar_tweets:
            if word in tweet and hashtag in tweet:
                prob_count += 1
        return prob_count/len(self.similar_tweets)

    def __hashtag_probability(self, hashtag):
        return self.all_haghtags[hashtag]/len(self.all_haghtags)

    def __get_all_hashtags(self):
        hashtags_res = {}
        for tweet in self.similar_tweets:
            for hashtag in additional_functions.get_hashtags_of_tweet(tweet):
                if hashtag in hashtags_res:
                    hashtags_res[hashtag] += 1
                else:
                    hashtags_res[hashtag] = 1
        return hashtags_res

if __name__ == "__main__":
    bayes = BayesClassificator()

    print(bayes.all_haghtags)

