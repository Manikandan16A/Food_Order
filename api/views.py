from django.http import JsonResponse

def food_items_list(request):
    return JsonResponse({"message": "List of food items will appear here."})
