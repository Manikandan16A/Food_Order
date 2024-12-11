from . import views  # Ensure this import is correct
from django.http import HttpResponse
from django.urls import path, include
from django.contrib import admin


def home(request):
    return HttpResponse("Welcome to Food Order API!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', home, name='home'),  # Root URL
    path('api/food-items/', include('api.urls')),  # API paths
]
