from django.contrib import admin

from hit_dakwerken.accounts.models import AppUser


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ['email']
    # list_filter = ['is_banned']
    # search_fields = ['full_name', 'email']