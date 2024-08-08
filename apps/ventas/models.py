from django.db import models
from django.core.validators import EmailValidator, MinValueValidator
from apps.productos.models import Producto

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(validators=[EmailValidator(message="Ingrese un correo electrónico válido")])
    
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'

class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(validators=[MinValueValidator(1, message="Ingrese valores mayores de cero")])
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def calcularTotal(self):
        return self.producto.precio * self.cantidad
    
    def save(self, *args, **kwargs):
        self.total = self.calcularTotal()
        super().save(*args, **kwargs)