from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

from apartment.models import Apartment


class LoginViewWithApartments(LoginView):
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
