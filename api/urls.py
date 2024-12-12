# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create the router and register the FoodItemViewSet
router = DefaultRouter()
router.register(r'food-items', views.FoodItemViewSet, basename='food-item')

# Include the router's URLs
urlpatterns = [
    path('', include(router.urls)),  # Automatically includes the food-items API routes
]
