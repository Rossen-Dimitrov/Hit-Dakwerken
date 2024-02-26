from django.urls import path
from hit_dakwerken.article.views import (
    ArticleCreateView,
    ArticleEditView,
    ArticleDetailsView,
    ArticleDeleteView
)

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create articles'),
    path('details/<int:pk>/', ArticleDetailsView.as_view(), name='details article'),
    path('edit/<int:pk>/', ArticleEditView.as_view(), name='edit article'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete article'),
]

