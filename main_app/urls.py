from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.books_index, name='index'),
    path('books/<int:book_id>/', views.books_detail, name='detail'),
    path('books/create', views.BookCreate.as_view(), name='books_create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='books_update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='books_delete'),
    path('books/<int:book_id>/add_reading', views.add_reading, name='add_reading'),
    path('books/<int:book_id>/assoc_translator/<int:translator_id>/', views.assoc_translator, name='assoc_translator'),
    path('books/<int:book_id>/unassoc_translator/<int:translator_id>/', views.unassoc_translator, name='unassoc_translator'),

    path('translators/', views.TranslatorList.as_view(), name='translators_index'),
    path('translators/<int:pk>/', views.TranslatorDetail.as_view(), name='translators_detail'),
    path('translators/create/', views.TranslatorCreate.as_view(), name='translators_create'),
    path('translators/<int:pk>/update/', views.TranslatorUpdate.as_view(), name='translators_update'),
    path('translators/<int:pk>/delete/', views.TranslatorDelete.as_view(), name='translators_delete'),
]