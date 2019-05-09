from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_frontPage, name="notLoggedIn"),
    path('apartment/', views.get_apartments, name="apartments")
]