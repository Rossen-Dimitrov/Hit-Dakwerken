from django.urls import path
from hit_dakwerken.project.views import ProjectListView, ProjectDetailView

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects'),
    path('details/<int:pk>/', ProjectDetailView.as_view(), name='project details'),
]