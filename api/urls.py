from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_items_list, name='food_items'),
]
