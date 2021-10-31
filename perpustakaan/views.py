from django.shortcuts import render
from perpustakaan.models import Buku

def buku(requst):
    books = Buku.objects.all()
    konteks = {
        'books': books,
    }
    return render(requst, 'buku.html', konteks)

def penerbit(requst):
    return render(requst, 'penerbit.html')