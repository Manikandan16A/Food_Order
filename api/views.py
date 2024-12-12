from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import FoodItem
from .serializers import FoodItemSerializer


from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    authentication_classes = [TokenAuthentication]



# APIView for handling general GET and POST operations
class FoodItemsAPIView(APIView):
    authentication_classes = [TokenAuthentication]  # Token-based authentication

    def get(self, request):
        # Retrieve all food items
        items = FoodItem.objects.all()
        serializer = FoodItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Add a new food item
        serializer = FoodItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
