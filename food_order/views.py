# food_order/views.py
from django.http import JsonResponse
from .models import FoodItem

def food_items_api(request):
    # Fetch all food items
    items = FoodItem.objects.all()
    # Convert data to JSON format
    food_list = list(items.values('id', 'name', 'price', 'image_url'))
    return JsonResponse(food_list, safe=False)
