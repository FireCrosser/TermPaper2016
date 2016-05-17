import nltk


class TweetPreprocessor(object):
    punctuation_signs = ['.', ',', '!', '?', '/', "'", '"', '`']

    def __init__(self, tweet):
        self.tweet = tweet.split(' ')
        self.__to_lowercase()
        self.__remove_ends_of_verbs()
        self.__remove_punctuations()
        self.__remove_stopwords()

    def __to_lowercase(self):
        """ Convert all words to lowercase """
        self.tweet = [word.lower() for word in self.tweet]

    def __remove_ends_of_verbs(self):
        """ Remove ends of verbs such as don't, aren't, haven't, etc. """
        self.tweet = [word[:-2] if word[-1] == 't' and word[-2] == "'" else word for word in self.tweet]

    def __remove_punctuations(self):
        """ Remove punctuation signs """
        for word_index in range(len(self.tweet)):
            word_list = [x for x in self.tweet[word_index] if x not in self.punctuation_signs]
            self.tweet[word_index] = "".join(word_list)

    def __remove_stopwords(self):
        """ Remove stopwords (most common words, which ha """
        stopwords = nltk.corpus.stopwords.words('english')
        self.tweet = [word for word in self.tweet if word not in stopwords]

    def get_tweet(self):
        return "".join(self.tweet)
