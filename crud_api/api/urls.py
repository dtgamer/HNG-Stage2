from django.urls import path
from . import views

urlpatterns = [
    path('api/<str:name>/', views.PersonAPIView.as_view(), name='person-crud'),
    path('api/', views.PersonAPIView.as_view(), name='person-create'),
]
