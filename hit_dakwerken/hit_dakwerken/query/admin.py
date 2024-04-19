from django.contrib import admin
from hit_dakwerken.query.models import Query


@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'published_on')
    list_filter = ('published_on', 'user')
    search_fields = ['user__email']
