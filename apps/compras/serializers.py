from rest_framework import serializers
from .models import Proveedor, Compra

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'
        read_only_fields = ('total',)