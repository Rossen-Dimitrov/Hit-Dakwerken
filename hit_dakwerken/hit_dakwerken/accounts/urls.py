from django.urls import path
from hit_dakwerken.accounts.views import (
    RegisterUserView,
    LoginUserView,
    LogoutsUserView,
    LogoutUserView,
    DetailsUserView
)

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('details/<int:pk>/', DetailsUserView.as_view(), name='profile details'),
    path('logouts/', LogoutsUserView.as_view(), name='logouts'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]
