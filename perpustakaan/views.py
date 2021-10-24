from django.shortcuts import render

def buku(requst):
    judul = ["belajar django","belajar python", "belajar bootstrap"]
    penulis = "wahyu ari nugroho"

    konteks = {
        'title': judul,
        'penulis': penulis
    }
    return render(requst, 'buku.html', konteks)

def penerbit(requst):
    return render(requst, 'penerbit.html')