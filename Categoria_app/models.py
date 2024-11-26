from django.db import models

# Create your models here.

class Categorias(models.Model):
    id_categoria=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=20)
    Cant_Prod=models.IntegerField()
    Descripcion=models.CharField( max_length=100)
    id_producto=models.SmallIntegerField()
    Fecha_Creacion=models.DateField( auto_now=False, auto_now_add=False)
    Ventas=models.IntegerField()
    def __str__(self):

        return self.nombre
