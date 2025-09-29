from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    # lab 5
    path('html5/text/formatting', views.text_formatting_view, name='text_formatting_page'),
    path('html5/listing', views.listing_page_view, name='listing_page'),
    path('html5/tables', views.tables_page_view, name='tables_page'),
    path('html5/links', views.links_page_view, name='links_page'),
]