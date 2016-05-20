import nltk
import re
import string
import html
from stemming import porter2


class TweetPreprocessor(object):
    def __init__(self, tweet="This is my 5-th tweet!"):
        self.tweet = tweet.split(' ')
        self.hashtags = [word for word in self.tweet if len(word) > 0 and word[0] == '#']
        self.replies = [word for word in self.tweet if len(word) > 0 and word[0] == '@']
        # self.tweet = [word for word in self.tweet if word not in self.hashtags_and_replies]
        # self.__encode()
        self.__remove_numbers()
        self.__to_lowercase()
        self.__remove_urls()
        self.__remove_small_words()
        self.__remove_stopwords()
        self.__remove_punctuations()
        self.__make_stemming()
        self.__clean_hashtags()
        self.tweet += self.hashtags + self.replies

    def __encode(self):
        for word_index in range(len(self.tweet)):
            re.sub(r'\w', '', self.tweet[word_index])
            self.tweet[word_index] = ''.join([i if ord(i) < 128 else '' for i in self.tweet[word_index]])

    def __remove_numbers(self):
        self.tweet = [word for word in self.tweet if not re.match(r'\d', word)]

    def __to_lowercase(self):
        """ Convert all words to lowercase """
        self.tweet = [word.lower() for word in self.tweet]

    def __remove_urls(self):
        self.tweet = [word for word in self.tweet if not self.is_url(word)]

    def __remove_punctuations(self):
        """ Remove punctuation signs """
        punctuation_signs = set(string.punctuation)
        temp_tweet = []
        for word_index in range(len(self.tweet)):
            word = [x for x in self.tweet[word_index] if x not in punctuation_signs]
            if len(word) != 0:
                temp_tweet.append(''.join(word))
        self.tweet = temp_tweet

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

    def __clean_hashtags(self):
        punctuation_signs = set(string.punctuation)
        cleaned_tags = []
        for tag in self.hashtags:
            cleaned_tag = []
            for ch in tag[1:]:
                if (ch in punctuation_signs and ch != '_') or ch.rstrip() == '':
                    break
                cleaned_tag.append(ch)
            cleaned_tags.append('#' + ''.join(cleaned_tag))
        self.hashtags = cleaned_tags


    @staticmethod
    def is_url(word):
        if re.match('^(?!www | www\.)[A-Za-z0-9_-]+\.+[A-Za-z0-9.\/%&=\?_:;-]+$', word) or \
                re.match('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', word):
            return True
        return False

    def get_tweet(self):
        return "".join(self.tweet)


if __name__ == "__main__":
    tweet = "New Your tries to make EU a pr3tty #panda_fg*http #kfc\ngf"
    pre = TweetPreprocessor(tweet)
    # print(pre.is_url("https://t.co/c66r8Mbr4I"))
    print(pre.tweet)
    # print(pre.hashtags)
