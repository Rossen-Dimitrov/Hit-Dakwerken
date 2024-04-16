from django.urls import path
from hit_dakwerken.article.views import (
    ArticleDetailsView,
)

urlpatterns = [
    path('details/<int:pk>/', ArticleDetailsView.as_view(), name='article details'),
    # path('edit/<int:pk>/', ArticleListView.as_view(), name='article edit'),
    # path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article delete'),
    # path('create/', ArticleCreateView.as_view(), name='articles create'),
]

