from django.core.validators import MinValueValidator
from django.db import models

from hit_dakwerken.query.models import Query


class Offer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(
        default=0,
        validators=[MinValueValidator(0)],
        null=False,
        blank=False,
    )
    query = models.OneToOneField(
        Query,
        on_delete=models.CASCADE,
    )
