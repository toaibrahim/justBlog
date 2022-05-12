from unicodedata import name
from django import views
from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path("register/",views.register_user,name='register'),
    path("login/",views.login_user,name='login'),
    path("logout/",views.logout_user,name='logout'),
]