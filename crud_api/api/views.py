from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person
from .serializers import PersonSerializer

class PersonAPIView(APIView):
    def get(self, request, name=None):
        if name:
            try:
                person = Person.objects.get(name=name)
                serializer = PersonSerializer(person)
                return Response(serializer.data)
            except Person.DoesNotExist:
                return Response({"detail": "Person not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            persons = Person.objects.all()
            serializer = PersonSerializer(persons, many=True)
            return Response(serializer.data)

    def post(self, request, name=None):
        if name:
            return Response({"detail": "Invalid URL for creating a new person"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, name):
        try:
            person = Person.objects.get(name=name)
        except Person.DoesNotExist:
            return Response({"detail": "Person not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name):
        try:
            person = Person.objects.get(name=name)
        except Person.DoesNotExist:
            return Response({"detail": "Person not found"}, status=status.HTTP_404_NOT_FOUND)

        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
