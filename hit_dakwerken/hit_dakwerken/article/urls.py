from django.urls import path
from hit_dakwerken.common import views

urlpatterns = [
    path('', views.home_page, name='list articles'),
    path('create/', views.projects, name='create articles'),
    path('edit/', views.about_us, name='edit articles'),
    # path('details/', views.login, name='details articles'),
    path('delete/', views.contacts, name='delete articles'),
]