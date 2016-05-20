from TagsRecommender.core import bayes_generator, knn_generator
import threading
import string
import queue

if __name__ == "__main__":
    thread = threading.Thread()
    # print(controller.get_recommendations(type="knn"))
    # print(controller.get_recommendations(type="bayes"))
    q = queue.Queue()
    bayesgenerator = bayes_generator.BayesHashtagsGenerator(screen_name="ChampionsLeague", current_tweet="Real Madrid makes me happy", number_of_hashtags=4)
    knngenerator = knn_generator.KnnHashtagsGenerator(screen_name="ChampionsLeague", current_tweet="Real Madrid makes me happy", number_of_hashtags=4)
    bayesgenerator.start()
    knngenerator.start()
    # if not bayesgenerator.isAlive():
    #     print(bayesgenerator.recommended_tags)
    # if not knngenerator.isAlive():
    #     print(knngenerator.recommended_tags)
    bayes = bayesgenerator.join()
    print(bayes)
