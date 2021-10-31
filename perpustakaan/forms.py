from django.forms import ModelForm
from perpustakaan.models import Buku

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'