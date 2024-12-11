from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FoodItem
from .serializers import FoodItemSerializer
from django.http import HttpResponse
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Welcome to the Food Order App API!",
        "endpoints": {
            "food_items": "/api/food-items/",
            "admin": "/admin/"
        }
    })


@api_view(['GET', 'POST'])
def food_items(request):
    if request.method == 'GET':
        items = FoodItem.objects.all()
        serializer = FoodItemSerializer(items, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FoodItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
