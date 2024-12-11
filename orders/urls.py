from django.urls import path
from .views import FoodItemListCreateView, OrderListCreateView

urlpatterns = [
    path('fooditems/', FoodItemListCreateView.as_view(), name='fooditem-list-create'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
]
