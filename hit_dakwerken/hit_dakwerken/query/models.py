from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from hit_dakwerken.accounts.models import AppUser
from validators import MaxImageSizeValidator

UserModel = get_user_model()

OFFER_TITLE_MAX_LENGTH = 250
OFFER_TITLE_MIN_LENGTH = 3
OFFER_CONTENT_MIN_LENGTH = 10
MAX_PHOTO_SIZE = 5.0


class Query(models.Model):
    description = models.TextField(
        validators=(
            validators.MinLengthValidator(OFFER_CONTENT_MIN_LENGTH),
        ),
    )
    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )

    published_on = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    edited_on = models.DateTimeField(
        auto_now=True,
        blank=False,
        null=False,
    )

    photo = models.ImageField(
        upload_to='offer_photos/',
        validators=(MaxImageSizeValidator(MAX_PHOTO_SIZE),),
        null=True,
        blank=True
    )

