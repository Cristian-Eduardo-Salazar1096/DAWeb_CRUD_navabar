from django.db import models

# Create your models here.

class Productos(models.Model):
    id_producto=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=20)
    precio=models.IntegerField()
    Cantidad=models.SmallIntegerField()
    Descripcion=models.CharField(max_length=100)
    Categoria=models.CharField(max_length=20)
    Fech_Cad=models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):

        return self.nombre