from django.urls import path

from .views import add_to_cart, OrderListView, update_status

urlpatterns = [
    #front-end
    path('list', OrderListView.as_view(), name='order-list'),
    path('update_status', update_status, name='update_status'),
    path('add_to_cart', add_to_cart, name='add_to_cart'),
     
]