books = [
  {'title': 'The Sandman', 'author': 'Neil Gaiman', 'genre': 'Comic', 'publish_year': 1989},
  {'title': 'American Gods', 'author': 'Neil Gaiman', 'genre': 'Fiction', 'publish_year': 2001},
]



from django.shortcuts import render

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def books_index(request):
  return render(request, 'books/index.html', {
    'books': books
  })
