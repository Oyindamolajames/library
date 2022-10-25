from django.test import TestCase
from django.urls import reverse

from .models import Book

# Create your tests here.


class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="A good title",
            subtitle="An excelent subtitle",
            author="Ogunsanya James",
            isbn="2839438394",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "A good title")
        self.assertEqual(self.book.subtitle, "An excelent subtitle")
        self.assertEqual(self.book.author, "Ogunsanya James")
        self.assertEqual(self.book.isbn, "2839438394")

    def test_book_listview(self):
        res = self.client.get(reverse("home"))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "An excelent subtitle")
        self.assertTemplateUsed(res, "books/book_list.html")
