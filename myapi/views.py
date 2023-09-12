from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .models import Person
from .serializers import PersonSerializer
from django.shortcuts import render


class PersonCreateView(APIView):
    def post(self, request: Request):
        data = request.data
        name = data.get("name")
        if not isinstance(name, str):
            return Response({"error": "name must be a string"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PersonSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonRetrieveUpdateDeleteView(APIView):
    def get(self, request: Request, pk):
        try:
            queryset = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PersonSerializer(instance=queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request: Request, pk):
        data = request.data
        name = data.get("name")
        if not isinstance(name, str):
            return Response({"error": "name must be a string"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            queryset = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        queryset.name = name
        serializer = PersonSerializer(instance=queryset, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request, pk):
        try:
            queryset = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
