from django.contrib import admin

from hit_dakwerken.project.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('photo', 'description', 'location', 'finish_date', 'date_of_publication')
