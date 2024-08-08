from rest_framework import viewsets
from .models import Cliente, Venta
from apps.productos.models import Inventario
from .serializers import ClienteSerializer, VentaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    
    def perform_create(self, serializer):
        venta : Venta = serializer.save()
        
        producto = venta.producto
        producto.generarMovimiento(venta.cantidad, 'salida')
        producto.save()
        
        inventario = Inventario(producto=producto, tipo='salida', cantidad=venta.cantidad)
        inventario.save()
