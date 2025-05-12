from django import forms

class ScrapeForm(forms.Form):
    url = forms.URLField(label='URL Target', widget=forms.URLInput(attrs={'class': 'form-control'}))
