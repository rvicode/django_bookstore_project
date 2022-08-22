from django.urls import reverse_lazy
from django.views import generic

from .models import Book


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price']
    template_name = 'books/book_create.html'
    success_url = reverse_lazy('book_list')
