from django.urls import path

import Userapp.views as userapp

from .apps import UserappConfig

app_name = UserappConfig.name

urlpatterns = [
    path("login/", userapp.login, name="login"),
    path("logout/", userapp.logout, name="logout"),
    path("register/", userapp.register, name="register"),
    path("edit/", userapp.edit, name="edit"),
    path("verify/<str:email>/<str:activation_key>/", userapp.verify, name="verify"),
]
