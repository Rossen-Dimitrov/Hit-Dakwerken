from django.contrib.auth import get_user_model
from django.db import models

from hit_dakwerken.query.models import Query

UserModel = get_user_model()


class Invoice(models.Model):
    ADDRESS = [
        'DAKGROEP NAESSENS',
        'Leenstraat 135'''
        '9870 Zulte'''
        'België'
    ]
    VAT_NUMBER = 'BE0445298492'

    invoice_number = models.IntegerField(
        unique=True,
        primary_key=True,
    )
    address = models.CharField(
        default=ADDRESS,
        max_length=len(ADDRESS),
    )
    invoice_date = models.DateField(
        auto_now_add=True,
    )
    expiry_date = models.DateField(
        blank=False,
        null=False,
    )
    vat_number = VAT_NUMBER

    # employe = models

    description = models.TextField(
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )
    query = models.ForeignKey(
        Query,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

