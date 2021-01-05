from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from class2.models import Book
from django.urls import reverse_lazy
# Create your views here.


class BookListView(ListView):
    model = Book
    #template_name = 'book_list.html'
    context_object_name = 'list_of_books'
    # defalt template = book_list.html
    # defalt context object = book_list


class BookDetail(DetailView):
    model = Book
    #template_name = 'book_detail.html'
    # defalt template = book_detail.html
    # defalt context object = book or object


class BookCreate(CreateView):
    model = Book
    fields = ('title', 'author', 'pages', 'price')
    #template_name = 'book_form.html'


class BookUpdate(UpdateView):
    model = Book
    fields = ('title', 'pages', 'price')
    #template_name = 'book_form.html'


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')
