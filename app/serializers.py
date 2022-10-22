from rest_framework import serializers
from .models import Tipo_Negocio,Negocio,Item
from drf_extra_fields.fields import Base64ImageField 

class TipoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tipo_Negocio
        fields = '__all__'




class ItemSerializer(serializers.ModelSerializer):
    imagen = Base64ImageField(required = False)
    class Meta:
        model = Item
        fields = '__all__'

class NegocioSerializer(serializers.ModelSerializer):
    imgperfil = Base64ImageField(required = False)
    imgportada = Base64ImageField(required = False)
    
    class Meta:
        model = Negocio
        # exclude = ['dueno','likes']
        fields = ['nombre','descripcion','tipo_Negocio','imgperfil','imgportada','ubicacion','horaEntrada','horaSalida','contactFacebook','contactInstagram','contactWEB','contactEmail','creado']


