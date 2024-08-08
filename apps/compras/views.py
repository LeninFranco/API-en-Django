from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from .models import Proveedor, Compra
from apps.productos.models import Inventario
from .serializers import ProveedorSerializer, CompraSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    
    def perform_create(self, serializer):
        compra : Compra = serializer.save()
        
        producto = compra.producto
        producto.generarMovimiento(compra.cantidad, 'entrada')
        producto.save()
        
        inventario = Inventario(producto=producto, tipo='entrada', cantidad=compra.cantidad)
        inventario.save()