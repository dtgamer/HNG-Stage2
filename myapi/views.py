from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person
from .serializers import PersonSerializer
from django.shortcuts import get_object_or_404

class PersonCreateView(APIView):
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonRetrieveUpdateDeleteView(APIView):
    def get(self, request, name):
        person = get_object_or_404(Person, name=name)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def put(self, request, name):
        person = get_object_or_404(Person, name=name)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name):
        person = get_object_or_404(Person, name=name)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
