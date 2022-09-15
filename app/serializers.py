from rest_framework import serializers
from .models import Tipo_Negocio,Negocio,Item

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Negocio
        fields = '__all__'


class NegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negocio
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
