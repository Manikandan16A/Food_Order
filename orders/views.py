from django.shortcuts import render
from rest_framework import generics
from .models import FoodItem, Order
from .serializers import FoodItemSerializer, OrderSerializer

# API for Food Items
class FoodItemListCreateView(generics.ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

# API for Orders
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
