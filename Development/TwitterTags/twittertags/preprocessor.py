import nltk
import re
import string
from stemming import porter2


class TweetPreprocessor(object):

    def __init__(self, tweet):
        self.tweet = tweet.split(' ')
        self.__remove_numbers()
        self.__to_lowercase()
        self.__remove_urls()
        self.__remove_punctuations()
        self.__remove_small_words()
        self.__remove_stopwords()
        self.__make_stemming()

    def __remove_numbers(self):
        self.tweet = [word for word in self.tweet if not re.match('[0-9]', word)]

    def __to_lowercase(self):
        """ Convert all words to lowercase """
        self.tweet = [word.lower() for word in self.tweet]

    def __remove_urls(self):
        self.tweet = [word for word in self.tweet if not self.is_url(word)]

    def __remove_punctuations(self):
        """ Remove punctuation signs """
        punctuation_signs = set(string.punctuation)
        for word_index in range(len(self.tweet)):
            word_list = [x for x in self.tweet[word_index] if x not in punctuation_signs]
            self.tweet[word_index] = "".join(word_list)

    def __remove_small_words(self):
        """ Remove words with length less than 3"""
        self.tweet = [word for word in self.tweet if not len(word) < 3]

    def __remove_stopwords(self):
        """ Remove stopwords (most common, function words """
        stopwords = nltk.corpus.stopwords.words('english')
        self.tweet = [word[:-2] if word[-1] == 't' and word[-2] == "'" else word for word in self.tweet]
        self.tweet = [word for word in self.tweet if word not in stopwords]

    def __make_stemming(self):
        self.tweet = [porter2.stem(word) for word in self.tweet]

    @staticmethod
    def is_url(word):
        if re.match('^(?!www | www\.)[A-Za-z0-9_-]+\.+[A-Za-z0-9.\/%&=\?_:;-]+$', word):
            return True
        return False

    def get_tweet(self):
        return "".join(self.tweet)

if __name__ == "__main__":
    tweet = "New Your tries to make EU a pretty panda"
    pre = TweetPreprocessor(tweet)
    print(pre.tweet)