from django.contrib import admin
from django.urls import path
from user import views
from django.contrib import auth



urlpatterns = [
    
    path("register/",views.register,name="register"),
    path("login/",views.loginUser,name="login"),
    path("logout/",views.logoutUser,name = "logout"),
    path("<int:id>/",views.profile,name="profile")
]
