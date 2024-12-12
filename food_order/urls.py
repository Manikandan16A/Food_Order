from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authtoken.views import obtain_auth_token


# Root view for the API
def root_view(request):
    return HttpResponse("Welcome to the Food Order API. Use /api/food-items/ to access the API.")

# Swagger Schema View
schema_view = get_schema_view(
    openapi.Info(
        title="Food Ordering API",
        default_version='v1',
        description="API documentation for the Food Ordering App",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your_email@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URL patterns
urlpatterns = [
    path('', root_view, name='root-view'),  # Root path for the API
    path('admin/', admin.site.urls),  # Admin site
    path('api/', include('api.urls')),  # Include app URLs
    # Swagger and ReDoc endpoints
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
