from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='login/login-index.html'), name='login'),
    path('register', views.register, name="register"),
    path('logout', LogoutView.as_view(next_page='login'), name='logout')
    ]