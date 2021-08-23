from django.urls import path
from .views import get_all_users, get_user_data, register_view

urlpatterns = [
    # Users
    path("all/", get_all_users),
    path("me/<id>", get_user_data),


    # Authentication
    path("auth/register/", register_view),
]
