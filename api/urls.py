from django.urls import path
from . import views

urlpatterns = [
    path('food-items/', views.food_items_list, name='food_items'),  # Add the 'food-items/' path
]
