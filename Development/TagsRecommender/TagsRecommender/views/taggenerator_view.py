from django.shortcuts import render_to_response, RequestContext, render, HttpResponseRedirect
from django.contrib import messages
from TagsRecommender.forms.recommendation_form import RecommendationForm
from TagsRecommender.core import bayes_generator, knn_generator


def get_recommendations(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST or None)
        if form.is_valid():
            screen_name = form.cleaned_data['screen_name']
            tweet = form.cleaned_data['tweet']
            bayesgenerator = bayes_generator.BayesHashtagsGenerator(screen_name=screen_name, current_tweet=tweet)
            knngenerator = knn_generator.KnnHashtagsGenerator(screen_name=screen_name, current_tweet=tweet)
            bayesgenerator.start()
            knngenerator.start()
            bayes_results = bayesgenerator.recommended_tags
            knn_results = knngenerator.recommended_tags
            recommended_tags = []
            for bayes_res in bayes_results:
                if bayes_res in knn_results:
                    recommended_tags.append(bayes_res)
                    bayes_results.pop(bayes_res)
                    knn_results.pop(bayes_res)
            while len(recommended_tags) < 4:
                for knn_res in knn_results:
                    recommended_tags.append(knn_res)
            while len(recommended_tags) < 4:
                for bayes_res in bayes_results:
                    recommended_tags.append(bayes_res)
            messages.success(request, messages.INFO, ' '.join(recommended_tags))
            return HttpResponseRedirect('/drivers')
    else:
        form = RecommendationForm()
        return render(request, 'TagsRecommender/main.html', {'form': form})




