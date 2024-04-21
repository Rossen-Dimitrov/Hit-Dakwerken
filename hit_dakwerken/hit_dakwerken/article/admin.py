from django.contrib import admin

from hit_dakwerken.article.forms import ArticleCreateForm
from hit_dakwerken.article.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_on', 'user_email']
    list_filter = ('title', 'published_on')
    search_fields = ['title']
    search_help_text = ['Search by title']

    @staticmethod
    def user_email(obj):
        users = obj.user.all()
        if users:
            return ', '.join(user.email for user in users)
        else:
            return 'N/A'
