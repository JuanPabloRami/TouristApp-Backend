from email.policy import default
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUserManager(BaseUserManager):
  def create_user(self,email,password,**extra_fields):
    email = self.normalize_email(email)
    user = self.model(
      email=email,
      **extra_fields
    )
    
    user.set_password(password)
    
    user.save()
    
  def create_superuser(self,email,password,**extra_fields):
    extra_fields.setdefault("is_staff",True)
    extra_fields.setdefault("is_superuser",True)
    
    if extra_fields.get("is_staff") is not True:
      raise ValueError("El superUsuario debe tener el is_staff en true ")
    
    if extra_fields.get("is_superuser") is not True:
      raise ValueError("El superUsuario debe tener el is_superuser en true ")
    
    return self.create_user(email = email,password=password,**extra_fields)
  
class User(AbstractUser):
  email = models.CharField(max_length=80,unique=True)
  username = models.CharField(max_length=45)
  first_name = models.CharField(max_length=60)
  last_name = models.CharField(max_length=60)
  image = models.ImageField(blank='', default = '',upload_to="users/")
  type_user = models.CharField(max_length = 45,default='')
  
  objects = CustomUserManager()
  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["first_name","last_name","username","type_user"]
  
  def __str__(self):
    return self.username
