from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_frontPage, name="login-index"),
    path('register', views.register, name='register')
    ]