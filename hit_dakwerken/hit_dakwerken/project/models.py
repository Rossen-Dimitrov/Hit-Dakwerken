from django.core.validators import MinLengthValidator
from django.db import models

from validators import MaxImageSizeValidator


class Project(models.Model):
    MAX_DESCRIPTION = 300
    MIN_DESCRIPTION = 10
    MAX_LOCATION = 30
    MAX_PHOTO_SIZE = 5.0

    photo = models.ImageField(
        upload_to='projects/',
        validators=(MaxImageSizeValidator(MAX_PHOTO_SIZE),),
        null=False,
        blank=True
    )

    description = models.TextField(
        validators=(
            MinLengthValidator(MIN_DESCRIPTION),
        ),
        max_length=MAX_DESCRIPTION,
        blank=False,
        null=False,
    )

    location = models.CharField(
        max_length=MAX_LOCATION,
        blank=False,
        null=False,
    )
    finish_date = models.DateTimeField(
        blank=True,
        null=True,
    )

    date_of_publication = models.DateTimeField(
        auto_now=True,
        blank=False,
        null=False,
    )
