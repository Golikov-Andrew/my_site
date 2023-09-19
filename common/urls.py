from django.urls import path

from .views import index
from .views.auth import LoginUser, profile, logout_user, RegisterUser

urlpatterns = [
    path('', index, name='homepage'),

    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_user, name='logout')
]
