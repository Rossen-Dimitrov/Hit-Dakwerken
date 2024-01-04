# from django.contrib.auth import models as auth_models, get_user_model
# from django.db import models
# from hit_dakwerken.accounts.managers import AppUserManager
#
# from django.conf import settings
# UserModel = settings.AUTH_USER_MODEL
# # UserModel = get_user_model()
#
#
# class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
#     USERNAME_FIELD = 'email'
#
#     objects = AppUserManager()
#
#     email = models.EmailField(
#         null=False,
#         blank=False,
#         unique=True,
#     )
#
#     is_staff = models.BooleanField(
#         default=False,
#     )
#
#
# class AppUserProfile(models.Model):
#     first_name = models.CharField(
#         max_length=50,
#         null=True,
#         blank=True,
#     )
#     last_name = models.CharField(
#         max_length=50,
#         null=True,
#         blank=True,
#     )
#
#     user = models.OneToOneField(
#         UserModel,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
