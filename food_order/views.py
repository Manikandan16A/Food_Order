from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FoodItemSerializer

class BulkFoodItemCreate(APIView):
    def post(self, request, *args, **kwargs):
        # Check if input is a list (bulk data) or a dictionary (single item)
        if isinstance(request.data, list):  
            # Handle bulk data (list of food items)
            serializer = FoodItemSerializer(data=request.data, many=True)
        else:
            # Handle single food item
            serializer = FoodItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
