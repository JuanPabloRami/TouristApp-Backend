from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Departamento(models.Model):
    nombre =models.TextField()
    codigo = models.IntegerField()

class Ciudad(models.Model):
    nombre =models.TextField()
    codigo = models.IntegerField()
    departamento = models.ForeignKey(Departamento,on_delete=models.PROTECT)

class Tipo_Negocio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imgCategoria = models.ImageField(blank='', default = '',upload_to="categorias/")
    def __str__(self):
        return self.nombre
        

class Negocio(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField()
    tipo_Negocio=models.ForeignKey(Tipo_Negocio,on_delete=models.PROTECT)
    imgperfil = models.ImageField(blank='', default = '',upload_to="negocios/")
    imgportada = models.ImageField(blank='', default = '',upload_to="negocios/")
    creado = models.DateTimeField(auto_now_add=True)
    ciudad = models.ForeignKey(Ciudad,on_delete=models.PROTECT)
    ubicacion = models.TextField(null = True)
    likes = models.IntegerField(default=0)
    dueno = models.ForeignKey(User, on_delete=models.CASCADE,related_name="negocios")
    horaEntrada = models.TimeField(null = True)
    horaSalida = models.TimeField(null = True)
    contactFacebook = models.TextField(null = True)
    contactInstagram= models.TextField(null = True)
    contactWEB =models.TextField(null = True)
    contactEmail = models.TextField(null = True)
    
    def __str__(self):
        return self.nombre

class Item(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField()
    precio=models.IntegerField()
    nuevo=models.BooleanField()
    imagen = models.ImageField(blank='', default = '',upload_to="negocios/items/")
    creado = models.DateTimeField(auto_now_add=True)
    negocio=models.ForeignKey(Negocio,on_delete=models.PROTECT)
    imgpromocion = models.ImageField(blank='',default='',upload_to="negocios/items/promociones/")
    
    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    comentario = models.CharField(max_length = 500)
    negocio=models.ForeignKey(Negocio,on_delete=models.PROTECT)
    autor = models.ForeignKey(User, on_delete=models.CASCADE,related_name="comentarios")
    creado = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    negocio=models.ForeignKey(Negocio,on_delete=models.PROTECT)
    autor = models.ForeignKey(User, on_delete=models.CASCADE,related_name="likes")




