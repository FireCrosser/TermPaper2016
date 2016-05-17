from twittertags.models.graph import Graph
from twittertags.preprocessor import TweetPreprocessor
import nltk

if __name__ == "__main__":
    tweet = "#Hello from the other... SidE! Don't worry, be happy!"
    pre = TweetPreprocessor(tweet)
    print(pre.tweet)
    # print(nltk.corpus.stopwords.words('english'))