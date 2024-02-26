from django.contrib import admin

from hit_dakwerken.article.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
