from django.db import models
from django.core.validators import MinValueValidator

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, null=True, on_delete=models.SET_NULL)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(validators=[MinValueValidator(0, message="Ingrese valores positivos")])
    
    def generarMovimiento(self, cantidad: int, tipo: str):
        if tipo == "entrada":
            self.stock += cantidad
        elif tipo == "salida":
            if self.stock - cantidad < 0:
                raise ValueError("Stock insuficiente")
            self.stock -= cantidad
        else:
            raise ValueError("Tipo de movimiento no válido")
    
    def __str__(self) -> str:
        return self.nombre

class Inventario(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=[('entrada', 'Entrada'), ('salida', 'Salida')])
    cantidad = models.IntegerField(validators=[MinValueValidator(1, message="Ingrese valores mayores de cero")])