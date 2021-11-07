from rest_framework.decorators import permission_classes
from perpustakaan.models import Kelompok
from perpustakaan.serializers import KelompokSerializers
from rest_framework import viewsets, permissions

class KelompokViewset(viewsets.ModelViewSet):
    queryset = Kelompok.objects.all()
    serializer_class = KelompokSerializers
    permission_classes = [permissions.IsAuthenticated]