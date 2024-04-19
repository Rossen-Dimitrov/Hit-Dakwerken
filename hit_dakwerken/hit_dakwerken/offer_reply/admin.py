from django.contrib import admin

from hit_dakwerken.offer_reply.models import Offer


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_filter = ('name', 'description', 'price')
    search_fields = ['name', 'description', 'price']


