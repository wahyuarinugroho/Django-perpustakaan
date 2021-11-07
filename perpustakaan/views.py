from django.http import response
from django.shortcuts import redirect, render, HttpResponse
from import_export import resources
from perpustakaan.models import Buku, Kelompok
from perpustakaan.forms import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from perpustakaan.resource import BukuResource

def export_xlsx(request):
    buku = BukuResource()
    dataset = buku.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=buku.xlsx'
    return response

@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"user berhasil dibuat")
            return redirect('signup')
        else:
            messages.error(request,"user gagal dibuat!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form' : form,
        }
        return render(request, 'signup.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST, request.FILES, instance=buku)
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

@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()
    messages.success(request, "data berhasil dihapus")
    return redirect('buku')


@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    # select * from buku a inner join kelompok b ON a.kelompok_id=b.id where b.name="produktif"
    # books = Buku.objects.filter(kelompok_id__nama='Produktif')
    #select * from buku
    books = Buku.objects.all()
    konteks = {
        'books': books,
    }
    return render(request, 'buku.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def penerbit(request):
    return render(request, 'penerbit.html')

@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
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