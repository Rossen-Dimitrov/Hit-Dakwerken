from django.urls import path
from hit_dakwerken.common import views
from hit_dakwerken.common.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('about_us/', views.about_us, name='about_us'),
    # path('contacts/', views.contacts, name='contacts'),
]