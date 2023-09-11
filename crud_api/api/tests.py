from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Person

class PersonAPITestCase(APITestCase):
    def setUp(self):
        self.person1 = Person.objects.create(name="John Doe")
        self.person2 = Person.objects.create(name="Jane Smith")
        self.valid_payload = {"name": "Alice Johnson"}
        self.invalid_payload = {"name": ""}

    def test_list_persons(self):
        url = reverse("person-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_person(self):
        url = reverse("person-list")
        response = self.client.post(url, self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_person(self):
        url = reverse("person-list")
        response = self.client.post(url, self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_person(self):
        url = reverse("person-detail", args=[self.person1.name])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_person(self):
        url = reverse("person-detail", args=[self.person1.name])
        response = self.client.put(url, self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_person(self):
        url = reverse("person-detail", args=[self.person1.name])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
