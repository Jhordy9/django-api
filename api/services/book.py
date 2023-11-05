from django.core import serializers
from api.forms.book import BookForm
from api.models.book import Book
from django.forms.models import model_to_dict


class BookService:
    @staticmethod
    def add_book(data):
        form = BookForm(data)
        if form.is_valid():
            return form.save()
        else:
            raise ValueError("Invalid book data")

    def book_list():
        books = Book.objects.all()
        books_json = serializers.serialize('json', books)
        return books_json

    def book_by_pk(pk: int):
        book = Book.objects.get(pk=pk)
        return model_to_dict(book)
