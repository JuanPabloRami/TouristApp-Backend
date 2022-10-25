from rest_framework import serializers
from .models import Tipo_Negocio,Negocio,Item,Comentario,Ciudad,Departamento
from drf_extra_fields.fields import Base64ImageField 

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class CiudadSerializer(serializers.ModelSerializer):
    departamento_id = serializers.PrimaryKeyRelatedField(queryset = Departamento.objects.all(), source="departamento")
    departamento = DepartamentoSerializer(read_only=True)
    class Meta:
        model = Ciudad
        fields = ['nombre','codigo','departamento_id','departamento']

class TipoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tipo_Negocio
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    imagen = Base64ImageField(required = False)
    class Meta:
        model = Item
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comentario
        exclude = ['autor']

class NegocioSerializer(serializers.ModelSerializer):
    imgperfil = Base64ImageField(required = False)
    imgportada = Base64ImageField(required = False)
    tipo_Negocio = TipoSerializer(read_only=True)
    tipo_Negocio_id = serializers.PrimaryKeyRelatedField(queryset = Tipo_Negocio.objects.all(), source="tipo_Negocio")
    ciudad = CiudadSerializer(read_only=True)
    ciudad_id = serializers.PrimaryKeyRelatedField(queryset = Ciudad.objects.all(), source="ciudad")
    
    class Meta:
        model = Negocio
        # exclude = ['dueno','likes']
        fields = ['nombre','descripcion','tipo_Negocio_id','tipo_Negocio','imgperfil','imgportada','ciudad_id','ciudad','ubicacion','horaEntrada','horaSalida','contactFacebook','contactInstagram','contactWEB','contactEmail','creado']


