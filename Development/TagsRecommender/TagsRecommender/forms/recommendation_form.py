from django import forms

class RecommendationForm(forms.Form):
    screen_name = forms.CharField(max_length=20)
    tweet = forms.CharField(max_length=140)

    def clean(self):
        cleaned_data = super(RecommendationForm, self).clean()
        screen_name = cleaned_data.get('screen_name')
        tweet = cleaned_data.get('tweet')
        if not screen_name or not tweet:
            raise forms.ValidationError()
