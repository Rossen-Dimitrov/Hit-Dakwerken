from django.urls import path
from hit_dakwerken.invoice import views
# from hit_dakwerken.invoice.views import InvoiceListView

urlpatterns = [
    path('', views.invoices, name='invoices'),
    # path('projects/', views.projects, name='projects page'),
    # path('about_us/', views.about_us, name='about_us page'),
    # path('contacts/', views.contacts, name='contacts page'),
    # path('login/', views.login, name='login page'),
]