from django import forms
from django.forms import ModelForm, widgets
from perpustakaan.models import Buku

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        # fungsi exclude - menampilkan data selain yg dipanggil
        # exclude = ['penerbit','jumlah']
        fields = '__all__'

        widgets = {
            'judul': forms.TextInput({'class':'form-control','id':'input judul','placeholder':'input judul'}),
            'penulis': forms.TextInput({'class':'form-control','id':'input penulis','placeholder':'input penulis'}),
            'penerbit': forms.TextInput({'class':'form-control','id':'input penerbit','placeholder':'input penerbit'}),
            'jumlah': forms.NumberInput({'class':'form-control','id':'input jumlah','placeholder':'input jumlah'}),
            'kelompok_id': forms.Select({'class':'form-control'}),
        }