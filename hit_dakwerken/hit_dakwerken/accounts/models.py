from django.contrib.auth import models as auth_models, get_user_model
from django.core import validators
from django.db import models
from hit_dakwerken.accounts.managers import AppUserManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_FIELD = 'email'

    objects = AppUserManager()

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )


UserModel = get_user_model()


class AppUserProfile(models.Model):
    NAME_MAX_LENGTH = 30
    NAME_MIN_LENGTH = 3
    COMPANY_NAME_MAX_LENGTH = 50
    COMPANY_NAME_MIN_LENGTH = 50
    COMPANY_URL_MAX_LENGTH = 255

    first_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(NAME_MIN_LENGTH),
        ),
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(NAME_MIN_LENGTH),
        ),
        null=True,
        blank=True,
    )

    company_position = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(NAME_MIN_LENGTH),
        ),
        null=True,
        blank=True,
    )

    company_name = models.CharField(
        max_length=COMPANY_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(COMPANY_NAME_MIN_LENGTH),
        ),
        null=True,
        blank=True,
    )
    company_url = models.URLField(
        max_length=COMPANY_URL_MAX_LENGTH,
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
