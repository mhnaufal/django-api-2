from django.urls import path
from .views import get_users_data, get_user_data

urlpatterns = [
    path('all/', get_users_data),
    path('me/<id>', get_user_data),
]
