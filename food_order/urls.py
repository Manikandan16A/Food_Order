from django.contrib import admin
from django.urls import path, include
from . import views

# Example data to be displayed at the root URL
def home(request):
    data = {
        "api_endpoints": {
            "food_items": "/api/food-items/",
            "orders": "/api/orders/",  # Example additional endpoint
        },
        "message": "Explore the Food Order API through the listed endpoints."
    }
    return JsonResponse(data)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include all URLs from api.urls
    path('', home, name='home'),  # Root URL
]
