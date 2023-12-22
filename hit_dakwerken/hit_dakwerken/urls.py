from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hit_dakwerken.common.urls')),
    # path('article/', include('hit_dakwerken.article.urls')),
    # path('customer/', include('hit_dakwerken.customer.urls')),
    # path('invoice/', include('hit_dakwerken.invoice.urls')),
    # path('offer/', include('hit_dakwerken.offer.urls')),
    # path('project/', include('hit_dakwerken.project.urls')),
    # path('request/', include('hit_dakwerken.request.urls')),
]
