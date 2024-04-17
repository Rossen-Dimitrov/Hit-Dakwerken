from django.db import models

from hit_dakwerken.query.models import Query


class Offer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(
        null=False,
        blank=False,
    )
    query = models.ForeignKey(
        Query,
        on_delete=models.CASCADE,
    )
