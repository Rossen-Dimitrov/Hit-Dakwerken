from django import forms
from django.core import validators
from hit_dakwerken.article.models import Article

ARTICLE_TITLE_MAX_LENGTH = 250
ARTICLE_TITLE_MIN_LENGTH = 3
ARTICLE_CONTENT_MIN_LENGTH = 10


class ArticleCreateForm(forms.ModelForm):
    title = forms.CharField(
        max_length=ARTICLE_TITLE_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(ARTICLE_TITLE_MIN_LENGTH),
        ),
    )

    content = forms.CharField(
        widget=forms.Textarea,
        validators=(
            validators.MinLengthValidator(ARTICLE_CONTENT_MIN_LENGTH),
        ),
    )

    image = forms.ImageField()

    class Meta:
        model = Article
        fields = ['title', 'content', 'image']
