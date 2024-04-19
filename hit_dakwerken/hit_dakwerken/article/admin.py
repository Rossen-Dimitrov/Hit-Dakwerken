from django.contrib import admin

from hit_dakwerken.article.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_on']
    list_filter = ('title', 'published_on')
    search_fields = ['title']
