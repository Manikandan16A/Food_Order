from . import views  # Ensure this import is correct
from django.http import HttpResponse
from django.urls import path, include

def home(request):
    return HttpResponse("Welcome to Food Order API!")

urlpatterns = [
    path('', home, name='home'),  # Root URL
    path('api/food-items/', include('api.urls')),  # API paths
]
