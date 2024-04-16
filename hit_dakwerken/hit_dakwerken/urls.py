from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from hit_dakwerken import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hit_dakwerken.common.urls')),
    path('accounts/', include('hit_dakwerken.accounts.urls')),
    path('invoices/', include('hit_dakwerken.invoice.urls')),
    path('ask/', include('hit_dakwerken.query.urls')),
    path('projects/', include('hit_dakwerken.project.urls')),
    path('article/', include('hit_dakwerken.article.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
