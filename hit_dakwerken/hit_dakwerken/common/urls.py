from django.urls import path, include
from hit_dakwerken.common import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('projects/', views.projects, name='projects'),
    path('about_us/', views.about_us, name='about_us'),
    path('contacts/', views.contacts, name='contacts'),
]