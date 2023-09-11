from django.urls import path
from .views import PersonAPIView

urlpatterns = [
    path('api/', PersonAPIView.as_view(), name='person-api'),  # Endpoint for CRUD operations on persons
]
