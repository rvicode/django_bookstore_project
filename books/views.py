from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic

from .models import Book


class BookListView(generic.ListView):
    model = Book
    paginate_by = 6
    template_name = 'books/book_list.html'
    context_object_name = 'books'


# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'
#     context_object_name = 'book'

def book_detail_view(request, pk):
    # get book object
    book = get_object_or_404(Book, pk=pk)
    # get book comments
    comment = book.comments.all()
    return render(request, 'books/book_detail.html', {'book': book, 'comment': comment})


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover', ]
    template_name = 'books/book_create.html'
    success_url = reverse_lazy('book_list')


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover', ]
    template_name = 'books/book_update.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
