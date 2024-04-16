from django.views.generic import DetailView
from django.views.generic.list import ListView
from hit_dakwerken.project.models import Project


class ProjectListView(ListView):
    template_name = 'project/project-list.html'
    model = Project


class ProjectDetailView(DetailView):
    template_name = 'project/project-details.html'
    model = Project
