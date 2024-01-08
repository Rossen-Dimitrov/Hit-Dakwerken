from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hit_dakwerken.common.urls')),
    path('accounts/', include('hit_dakwerken.accounts.urls')),
    path('invoices/', include('hit_dakwerken.invoice.urls')),
    path('articles/', include('hit_dakwerken.article.urls')),
    # path('offers/', include('hit_dakwerken.offer.urls')),
    # path('projects/', include('hit_dakwerken.project.urls')),
    # path('requests/', include('hit_dakwerken.request.urls')),
]
