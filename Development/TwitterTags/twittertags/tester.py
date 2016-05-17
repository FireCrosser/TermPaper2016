import json
from twittertags.preprocessor import TweetPreprocessor

if __name__ == "__main__":
    with open('json_data/users_tweets.json') as data_file:
        data = json.load(data_file)
    print(len(data))