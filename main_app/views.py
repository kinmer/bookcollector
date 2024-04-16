from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Book, Translator
from .forms import ReadingForm


def home(request):
    return render(request, 'home.html')

def about(request):
     return render(request, 'about.html')

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {
        'books': books
    })

def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    id_list = book.translators.all().values_list('id')
    translators_book_doesnt_have = Translator.objects.exclude(id__in=id_list)
    reading_form = ReadingForm()
    return render(request, 'books/detail.html', { 
        'book': book, 'reading_form': reading_form,
        'translators': translators_book_doesnt_have
})

def add_reading(request, book_id):
    form = ReadingForm(request.POST)
    if form.is_valid():
        new_reading = form.save(commit=False)
        new_reading.book_id = book_id
        new_reading.save()
    return redirect('detail', book_id=book_id)

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'genre', 'introduction', 'publish_year']

class BookUpdate(UpdateView):
    model = Book
    fields = ['author', 'genre', 'introduction', 'publish_year']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books'

class TranslatorList(ListView):
    model = Translator

class TranslatorDetail(DetailView):
    model = Translator

class TranslatorCreate(CreateView):
    model = Translator
    fields = '__all__'

class TranslatorUpdate(UpdateView):
    model = Translator
    fields = ['name', 'language']

class TranslatorDelete(DeleteView):
    model = Translator
    success_url = '/translators'

def assoc_translator(request, book_id, translator_id):
    Book.objects.get(id=book_id).translators.add(translator_id)
    return redirect('detail', book_id=book_id)

def unassoc_translator(request, book_id, translator_id):
    Book.objects.get(id=book_id).translators.remove(translator_id)
    return redirect('detail', book_id=book_id)