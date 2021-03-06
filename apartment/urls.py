from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="apartment-index"),
    path('<int:id>', views.get_apartment_by_id, name="apartment_details"),
    path('add_apartment', views.add_apartment, name="add_apartment"),
    path('delete_apartment/<int:id>', views.delete_apartment, name="delete_apartment"),
    path('buy_apartment/<int:id>', views.buy_apartment, name="buy_apartment"),
    path('update_apartment/<int:id>', views.update_apartment, name="update_apartment"),
    path('payment_success', views.payment_success, name="payment_success"),
    path('add_openhouse', views.add_openhouse, name="add_openhouse"),
    path('update_openhouse/<int:id>', views.update_openhouse, name="update_openhouse"),
    path('delete_openhouse/<int:id>', views.delete_openhouse, name="delete_openhouse"),
]
