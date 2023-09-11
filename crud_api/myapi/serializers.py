from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name',)

    def validate_name(self, value):
        # Add validation logic here if needed
        # For example, ensuring that the name is not empty
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value
