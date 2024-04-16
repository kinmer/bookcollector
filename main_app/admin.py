from django.contrib import admin

# Register your models here.
from .models import Book, Reading, Translator

admin.site.register(Book)
admin.site.register(Reading)
admin.site.register(Translator)