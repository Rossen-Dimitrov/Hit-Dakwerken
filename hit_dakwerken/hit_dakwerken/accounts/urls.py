from django.urls import path
from hit_dakwerken.accounts.views import (
    RegisterUserView,
    LoginUserView,
    DetailsUserView,
    EditUserView,
    DeleteUserView,
    logout_view
)

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('details/<int:pk>/', DetailsUserView.as_view(), name='profile details'),
    path('edit/<int:pk>/', EditUserView.as_view(), name='profile edit'),
    path('delete/<int:pk>/', DeleteUserView.as_view(), name='profile delete'),
    path('logout/', logout_view, name='logout'),
]
