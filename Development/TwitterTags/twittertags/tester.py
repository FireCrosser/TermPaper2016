import json
from twittertags import preprocessor
from twittertags import additional_functions
from twittertags import naivebayes_classification

if __name__ == "__main__":
    with open('json_data/users_tweets.json') as data_file:
        data = json.load(data_file)
    tweets = [entry[1] for entry in data]
    prepro = preprocessor.TweetPreprocessor()
    for tweet_index in range(len(tweets)):
        prepro = preprocessor.TweetPreprocessor(tweets[tweet_index])
        tweets[tweet_index] = prepro.tweet
    curr_tweet = "@LeBron goes baseline with @DeRozan Thompson"
    prepro = preprocessor.TweetPreprocessor(curr_tweet)
    tweets = additional_functions.similar_tweets(words=prepro.tweet, tweets=tweets)
    bayes = naivebayes_classification.BayesClassificator(curr_tweet, tweets, 2)
    print(bayes.all_haghtags)
    print(bayes.get_hashtags())