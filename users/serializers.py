from ast import Expression
from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str,smart_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import  get_current_site
from django.urls import reverse
from .utils import Util
from .models import User

from app.serializers import NegocioSerializer,ItemSerializer
from drf_extra_fields.fields import Base64ImageField 



class SignUpSerializer(serializers.ModelSerializer):
    
    first_name = serializers.CharField(max_length = 60)
    last_name = serializers.CharField(max_length = 60)
    email = serializers.CharField(max_length = 80)
    username= serializers.CharField(max_length = 45)
    password = serializers.CharField(min_length = 8,write_only=True)
    image = Base64ImageField(required = False)
    type_user = serializers.CharField(required=True)
    class Meta:
        model = User
        fields= ['first_name','last_name','image','email','username','password','type_user']
        
    def validate(self, attrs):
        email_exists=User.objects.filter(email = attrs['email']).exists()
        username_exists=User.objects.filter(username = attrs['username']).exists()

        if email_exists:
            raise ValidationError("Este correo ya esta en uso")

        if username_exists:
            raise ValidationError("Este nombre de usuario ya esta en uso")
        
        return super().validate(attrs)
    
    def create(self,validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)
        
        user.set_password(password)
        
        user.save()

        Token.objects.create(user=user)
        
        return user


class CurrentUserNegocioSerializer(serializers.ModelSerializer):
    negocios = NegocioSerializer(many = True)

    class Meta:
        model = User
        fields=['first_name','last_name','image','email','username','type_user','negocios']


class ResetPwEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ['email']

    def validate(self,attrs):
        
        email = attrs['data'].get('email','')
        

        # return super().validate(attrs)
