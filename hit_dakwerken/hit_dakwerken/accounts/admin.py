from hit_dakwerken.accounts.models import AppUser, AppUserProfile
from django.contrib import admin
from django.db.models import Q


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name')
    list_filter = ('email',)
    search_fields = ('email',)
    search_help_text = ['Search by email']


@admin.register(AppUserProfile)
class AppUserProfileAdmin(admin.ModelAdmin):
    list_display = ('get_user_email', 'first_name', 'last_name', 'company_name')
    list_filter = ('first_name', 'last_name', 'company_name')

    def get_user_email(self, obj):
        return obj.user.email

    get_user_email.short_description = 'User Email'

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        search_words = search_term.strip().split()

        user_email_queries = [Q(user__email__icontains=word) for word in search_words]

        user_email_query = Q()
        for q in user_email_queries:
            user_email_query |= q

        queryset |= self.model.objects.filter(user_email_query)

        return queryset, use_distinct
