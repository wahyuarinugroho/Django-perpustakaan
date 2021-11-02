from django.shortcuts import redirect, render
from perpustakaan.models import Buku, Kelompok
from perpustakaan.forms import FormBuku
from django.contrib import messages


def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diperbaharui")
            return redirect('ubah_buku', id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form': form,
            'buku': buku,
        }
    return render(request, template, konteks)

def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    
    buku.delete()
    return redirect('buku')

def buku(request):
    # select * from buku a inner join kelompok b ON a.kelompok_id=b.id where b.name="produktif"
    # books = Buku.objects.filter(kelompok_id__nama='Produktif')
    #select * from buku
    books = Buku.objects.all()
    konteks = {
        'books': books,
    }
    return render(request, 'buku.html', konteks)


def penerbit(request):
    return render(request, 'penerbit.html')


def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            form = FormBuku()
            messages.success(request, "Data Berhasil Ditambah")
            konteks = {
                'form' : form,
            }
            return render(request,'tambah-buku.html', konteks)
    else:
        form = FormBuku()
        konteks = {
            'form': form,
        }
    return render(request, 'tambah-buku.html', konteks)