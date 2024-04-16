from django.urls import path, include
from hit_dakwerken.query.views import QueryDetailsView, QueryCreateView, QueryEditView, QueryDeleteView

urlpatterns = [
    path('', include([
        path('create/', QueryCreateView.as_view(), name='query request create'),
        path('<int:pk>/', QueryDetailsView.as_view(), name='query request details'),
        path('<int:pk>/edit/', QueryEditView.as_view(), name='query request edit'),
        path('<int:pk>/delete/', QueryDeleteView.as_view(), name='query request delete'),
    ])),
]
