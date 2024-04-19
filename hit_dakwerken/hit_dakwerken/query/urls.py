from django.urls import path, include
from hit_dakwerken.query.views import QueryCreateView, QueryEditView, QueryDeleteView

urlpatterns = [
    path('', include([
        path('create/', QueryCreateView.as_view(), name='query create'),
        # path('<int:pk>/', QueryDetailsView.as_view(), name='query details'),
        path('<int:pk>/edit/', QueryEditView.as_view(), name='query edit'),
        path('<int:pk>/delete/', QueryDeleteView.as_view(), name='query delete'),
    ])),
]
