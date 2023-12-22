# from django.core import validators
# from django.db import models
#
#
# class Article(models.Model):
#     title = models.CharField(
#         max_length=250,
#         validators=[
#             validators.MinLengthValidator(3),
#         ],
#         null=False,
#         blank=False,
#     )
#     content = models.TextField(
#         validators=[
#             validators.MinLengthValidator(10),
#         ],
#     )
#     authors = models.ManyToManyField(
#         to=HitUser,
#         related_name='articles'
#     )
#     published_on = models.DateTimeField(
#         auto_now_add=True,
#         editable=False,
#     )
