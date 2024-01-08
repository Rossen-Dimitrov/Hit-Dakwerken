from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

UserModel = get_user_model()


class Article(models.Model):
    title = models.CharField(
        max_length=250,
        validators=(
            validators.MinLengthValidator(3),
        ),
    )
    content = models.TextField(
        validators=(
            validators.MinLengthValidator(10),
        ),
    )
    authors = models.ManyToManyField(
        to=UserModel,
        related_name='articles',
    )

    published_on = models.DateTimeField(
        auto_now_add=True,
    )

    edited_on = models.DateTimeField(
        auto_now=True,
    )

    image = models.ImageField(
        upload_to='static/images/',
        null=True,
        blank=True,
    )
