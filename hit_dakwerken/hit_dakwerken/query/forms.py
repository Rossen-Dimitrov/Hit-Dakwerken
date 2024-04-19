from django import forms
from django.core import validators
from hit_dakwerken.query.models import Query

OFFER_TITLE_MAX_LENGTH = 250
OFFER_TITLE_MIN_LENGTH = 3
OFFER_CONTENT_MIN_LENGTH = 10


class QueryBaseForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['description',]
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Describe your query'})
        }


class QueryCreateForm(QueryBaseForm):
    class Meta:
        model = Query
        fields = ['description', 'photo']

        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Describe your query'})
        }


class QueryEditForm(QueryBaseForm):
    class Meta:
        model = Query
        fields = ['description']

        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Describe your query'})
        }
