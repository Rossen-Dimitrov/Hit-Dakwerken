from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models


UserModel = get_user_model()

ARTICLE_TITLE_MAX_LENGTH = 250
ARTICLE_TITLE_MIN_LENGTH = 3
ARTICLE_CONTENT_MIN_LENGTH = 10


class Article(models.Model):
    title = models.CharField(
        max_length=ARTICLE_TITLE_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(ARTICLE_TITLE_MIN_LENGTH),
        ),
    )
    content = models.TextField(
        validators=(
            validators.MinLengthValidator(ARTICLE_CONTENT_MIN_LENGTH),
        ),
    )
    user = models.ManyToManyField(
        to=UserModel,
        # related_name='articles',
    )

    published_on = models.DateField(
        auto_now_add=True,
    )

    edited_on = models.DateField(
        auto_now=True,
    )

    image = models.ImageField(
        upload_to='static/images/',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

