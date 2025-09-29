from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))

def viewbook(request, bookId):
    books = {
        123: {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley', 'image': 'book1.jpg'},
        456: {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam', 'image': 'book2.jpg'},
        789: {'id': 789, 'title': 'Learning Python', 'author': 'M. Lutz', 'image': 'book3.jpg'},
        101: {'id': 101, 'title': 'JavaScript: The Good Parts', 'author': 'D. Crockford', 'image': 'book4.jpg'},
        112: {'id': 112, 'title': 'Design Patterns: Elements of Reusable Object-Oriented Software', 'author': 'Gang of Four', 'image': 'book5.jpg'},
        131: {'id': 131, 'title': 'The Pragmatic Programmer', 'author': 'A. Hunt and D. Thomas', 'image': 'book6.jpg'},
        415: {'id': 415, 'title': 'Clean Code', 'author': 'R. C. Martin', 'image': 'book7.jpg'},
        161: {'id': 161, 'title': 'Refactoring', 'author': 'M. Fowler', 'image': 'book8.jpg'},
        718: {'id': 718, 'title': "You Don't Know JS: Scope & Closures", 'author': 'K. Simpson', 'image': 'book9.jpg'},
        192: {'id': 192, 'title': 'Eloquent JavaScript', 'author': 'M. Haverbeke', 'image': 'book10.jpg'},
    }
    book = books.get(bookId)
    return render(request, 'bookmodule/one_book.html', {'book': book})

def list_books(request):
    books = [
        {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley', 'image': 'book1.jpg'},
        {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam', 'image': 'book2.jpg'},
        {'id': 789, 'title': 'Learning Python', 'author': 'M. Lutz', 'image': 'book3.jpg'},
        {'id': 101, 'title': 'JavaScript: The Good Parts', 'author': 'D. Crockford', 'image': 'book4.jpg'},
        {'id': 112, 'title': 'Design Patterns: Elements of Reusable Object-Oriented Software', 'author': 'E. Gamma, R. Helm, R. Johnson, J. Vlissides', 'image': 'book5.jpg'},
        {'id': 131, 'title': 'The Pragmatic Programmer', 'author': 'A. Hunt and D. Thomas', 'image': 'book6.jpg'},
        {'id': 415, 'title': 'Clean Code: A Handbook of Agile Software Craftsmanship', 'author': 'R. C. Martin', 'image': 'book7.jpg'},
        {'id': 161, 'title': 'Refactoring: Improving the Design of Existing Code', 'author': 'M. Fowler', 'image': 'book8.jpg'},
        {'id': 718, 'title': "You Don't Know JS: Scope & Closures", 'author': 'K. Simpson', 'image': 'book9.jpg'},
        {'id': 192, 'title': 'Eloquent JavaScript: A Modern Introduction to Programming', 'author': 'M. Haverbeke', 'image': 'book10.jpg'},
    ]
    return render(request, 'bookmodule/list_books.html', {'books': books})


def index(request):
    return render(request, "bookmodule/index.html")

def viewbook(request, bookId):
    return render(request, "bookmodule/one_book.html")

def aboutus(request):
    return render(request, "bookmodule/aboutus.html")


def links_page_view(request):
    return render(request, 'bookmodule/links.html')

def text_formatting_view(request):
    return render(request, 'bookmodule/text_formatting.html')

def listing_page_view(request):
    return render(request, 'bookmodule/listing.html')

def tables_page_view(request):
    return render(request, 'bookmodule/tables.html')