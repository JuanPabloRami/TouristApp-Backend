from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from rest_framework import status, viewsets

from .models import Tipo_Negocio,Negocio,Item
from .serializers import TipoSerializer,NegocioSerializer,ItemSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo_Negocio.objects.all()
    serializer_class= TipoSerializer
    permission_classes = [IsAuthenticated]

class NegocioViewSet(viewsets.ModelViewSet):
    queryset = Negocio.objects.all()
    serializer_class= NegocioSerializer
    

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class= ItemSerializer
    

def index(request):
    return render(request, 'index.html')





