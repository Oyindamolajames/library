from django.urls import  reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "Plant Breeding",
            subtitle = "Principles of plant breeding",
            author = "Williams S.  Vincent",
            isbn = "1234567890"
        )

    def test_api_listview(self):
        res = self.client.get(reverse("book_list"))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(res, self.book)   