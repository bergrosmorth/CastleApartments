from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from . import views

from apartment.models import Apartment


class AuthFormWithNewMessage(AuthenticationForm):
    error_messages = {
        'invalid_login':
            "HAHAHAHAAH! Please enter a correct %(username)s and password. Note that both fields may be case-sensitive.",
        'inactive': "This account is inactive."
    }


class LoginViewWithApartments(LoginView):
    form_class = AuthFormWithNewMessage

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        new_context = super(LoginView, self).get_context_data(**kwargs)
        new_context['apartments'] = Apartment.objects.all()
        return new_context




urlpatterns = [
    path('', LoginViewWithApartments.as_view(template_name='login/login-index.html'), name='login'),
    path('register', views.register, name="register"),
    path('logout', LogoutView.as_view(next_page='/'), name='logout')
    ]
