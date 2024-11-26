from django.db import models

# Create your models here.

class Pedidos(models.Model):
    id_pedido=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    fech=models.DateField(auto_now=False, auto_now_add=False)
    id_Cliente=models.SmallIntegerField()
    Costo=models.IntegerField()
    Direccion=models.CharField(max_length=100)
    Cantidad=models.IntegerField()
    def __str__(self):

        return self.nombre