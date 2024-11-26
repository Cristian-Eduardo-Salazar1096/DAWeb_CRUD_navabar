from django.db import models

# Create your models here.

class Provedores(models.Model):
    id_provedor=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=20)
    Producto=models.CharField(max_length=20)
    Sucursal=models.CharField( max_length=50)
    HorarioE=models.TimeField( auto_now=False, auto_now_add=False)
    HorarioS=models.TimeField( auto_now=False, auto_now_add=False)
    Producto_Cant=models.CharField(max_length=20)
    Direccion=models.CharField(max_length=40)
    def __str__(self):

        return self.nombre