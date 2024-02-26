from django.contrib import admin

from hit_dakwerken.accounts.models import AppUser, AppUserProfile


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'get_first_name', 'get_last_name']

    def get_first_name(self, obj):
        return obj.appuserprofile.first_name if obj.appuserprofile else 'N/A'

    def get_last_name(self, obj):
        return obj.appuserprofile.last_name if obj.appuserprofile else 'N/A'

    get_first_name.short_description = 'First Name'
    get_last_name.short_description = 'Last Name'


@admin.register(AppUserProfile)
class AppUserProfileAdmin(admin.ModelAdmin):
    pass
