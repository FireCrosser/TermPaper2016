from django.shortcuts import render_to_response, RequestContext, render
from django.contrib import messages
from TagsRecommender.forms.recommendation_form import RecommendationForm
from TagsRecommender.core import bayes_generator


def get_recommendations(request):
    form = RecommendationForm(request.POST or None)
    if form.is_valid():
        screen_name = form.cleaned_data['screen_name']
        tweet = form.cleaned_data['tweet']
        tags = bayes_generator.get_recommendations(screen_name=screen_name, curr_tweet=tweet)
        messages.success(request, messages.INFO, ' '.join(tags))
    return render_to_response('TagsRecommender/main.html', locals(), context_instance=RequestContext(request))




