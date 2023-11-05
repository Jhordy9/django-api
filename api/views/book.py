from django.http import Http404, HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json

from api.models.book import Book
from api.services.book import BookService


@require_http_methods(["GET"])
def book_list(_):
    books = BookService.book_list()
    return HttpResponse(books, content_type="application/json")


@require_http_methods(["GET"])
def book_by_pk(_, pk: int):
    try:
        book = BookService.book_by_pk(pk)
        return JsonResponse(book, content_type="application/json")
    except Book.DoesNotExist:
        raise Http404("Book does not exist")


@require_http_methods(["POST"])
@csrf_exempt
def add_book(request):
    try:
        book_data = json.loads(request.body.decode('utf-8'))
        book = BookService.add_book(book_data)
        return HttpResponse(book, status=201)
    except:
        return HttpResponseBadRequest('Invalid data provided for the book.')
