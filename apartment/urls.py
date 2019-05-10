from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="apartment-index"),
    path('<int:id>', views.get_apartment_by_id, name="apartment_details"),
    path('add_apartment', views.add_apartment, name="add_apartment"),
    path('delete_apartment/<int:id>', views.delete_apartment, name="delete_apartment" )
]