from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from .models import Categoria, Producto, Inventario
from .serializers import CategoriaSerializer, ProductoSerializer, InventaerioSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventaerioSerializer