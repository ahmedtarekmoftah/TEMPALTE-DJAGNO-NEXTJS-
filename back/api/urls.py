from django.urls import path, include
from rest_framework.routers import DefaultRouter



router = DefaultRouter()

urlpatterns = [
    # Router-generated endpoints
    path('', include(router.urls)),

    # Simple endpoints
  
]