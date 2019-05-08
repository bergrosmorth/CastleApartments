from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="apartment-index"),
    path('apartment/', views.get_apartments, name="apartments")
]