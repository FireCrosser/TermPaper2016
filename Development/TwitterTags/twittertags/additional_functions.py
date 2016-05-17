import math
import operator


def similar_tweets(words, tweets, num_of_main_words=3):
    words_frequency = {}
    for tweet_index in range(len(tweets)):
        for word in words:
            if word in tweets[tweet_index]:
                if word in words_frequency:
                    words_frequency[word] += 1
                else:
                    words_frequency[word] = 1
    tweets_len = len(tweets)
    for word in words_frequency:
        words_frequency[word] = math.log(tweets_len/words_frequency[word])
    unique_words = []
    for i in range(num_of_main_words):
        if len(words_frequency) == 0:
            break
        curr_max = max(words_frequency.items(), key=operator.itemgetter(1))[0]
        unique_words.append(curr_max)
        words_frequency.pop(curr_max)
    result_tweets_list = []
    for tweet in tweets:
        for word in unique_words:
            if word in tweet:
                result_tweets_list.append(tweet)
                break
    return result_tweets_list


def word_weight(word):
    if word[0] == '@':
        return 3
    else:
        return 1 + 0.1*len(word)


def __get_max_values_of_dict(dictionary, amount=3):
    sorted_tuples = ((k, dictionary[k]) for k in sorted(dictionary, key=dictionary.get, reverse=True))
    result = {}
    for k, v in sorted_tuples:
        result[k] = v
    return result


if __name__ == "__main__":
    tweet = "this is my tweet".split(" ")
    all_tweets = ["that is your tweet baby".split(" "), "mommy".split(" ")]
    tweets = similar_tweets(tweet, all_tweets, 2)
    print(tweets)
