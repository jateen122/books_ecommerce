from django.shortcuts import render, redirect, get_object_or_404
from .models import Book


def books(request):
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        book_description = request.POST.get('book_description')
        book_image = request.FILES.get('book_image')

        Book.objects.create(
            book_name=book_name,
            book_description=book_description,
            book_image=book_image
        )
        return redirect('/')

    queryset = Book.objects.all()
    context = {'books': queryset}
    return render(request, 'books.html', context)


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('/')


def update_book(request, id):
    queryset = Book.objects.get (id=id)
    context ={'book':queryset}
    return render(request,'updatebooks.html',context)


def login_page(request):
    return render(request, 'login.html')