from django.urls import path
from .views import PersonCreateView, PersonRetrieveUpdateDeleteView

urlpatterns = [
    path('api/', PersonCreateView.as_view(), name='person-create'),  # CREATE: Adding a new person
    path('api/<int:pk>', PersonRetrieveUpdateDeleteView.as_view(), name='person-retrieve-update-delete'),  # READ, UPDATE, DELETE
]
