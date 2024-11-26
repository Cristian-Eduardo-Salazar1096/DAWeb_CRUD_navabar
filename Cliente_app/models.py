from django.db import models

# Create your models here.

class Clientes(models.Model):
    id_cliente=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    Membresia=models.CharField(max_length=100)
    Fech_Nac=models.DateField( auto_now=False, auto_now_add=False)
    Telefono=models.IntegerField()
    Correo=models.CharField(max_length=100)
    Curp=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre