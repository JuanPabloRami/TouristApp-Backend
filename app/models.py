from django.db import models
from users.models import User

# Create your models here.

class Tipo_Negocio(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
        

class Negocio(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField()
    tipo_Negocio=models.ForeignKey(Tipo_Negocio,on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="negocios",null=True)
    dueno = models.ForeignKey(User, on_delete=models.PROTECT)

class Item(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField()
    precio=models.IntegerField()
    nuevo=models.BooleanField()
    imagen = models.ImageField(upload_to="negocios/items",null=True)
    negocio=models.ForeignKey(Tipo_Negocio,on_delete=models.PROTECT)