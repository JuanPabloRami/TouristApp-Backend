
from django.shortcuts import render,redirect, get_object_or_404
from rest_framework import status, viewsets, generics,mixins
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import APIView,api_view, permission_classes

from users.permissions import EsGrupoEmprendedor, EsGrupoTurista, EsIpPermitida

from .models import Tipo_Negocio,Negocio,Item,Comentario,Departamento,Ciudad
from .serializers import TipoSerializer,NegocioSerializer,ItemSerializer,DepartamentoSerializer,CiudadSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser,AllowAny
from .permissions import ReadOnly, AuthorOrReadOnly
from users.serializers import CurrentUserNegocioSerializer
#filtrado
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class= DepartamentoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class= CiudadSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'nombre':['contains'],
        'departamento__nombre':['contains']
        
    }

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo_Negocio.objects.all()
    serializer_class= TipoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre']




class NegocioListAndCreateView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class= NegocioSerializer
    queryset=Negocio.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'nombre':['contains'],
        'ubicacion':['contains'],
        'ciudad__nombre':['contains'],
        'ciudad__departamento__nombre':['contains'],
        'tipo_Negocio__nombre':['contains'],
        'id':['contains']
    }

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(dueno=user)
        return super().perform_create(serializer)

    

    def get(self,request:Request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post(self,request:Request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    

class NegocioRetrieveUpdateDeleteView(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class= NegocioSerializer
    queryset=Negocio.objects.all()
    permission_classes = [AuthorOrReadOnly]


    
    def get(self,request:Request,*args,**kwargs):
        
        return self.retrieve(request,*args,**kwargs)

    def put(self,request:Request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request:Request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


@api_view(http_method_names=['GET'])
@permission_classes([IsAuthenticated])
def get_negocios_for_current_user(request:Request):
    user=request.user
    serializer=CurrentUserNegocioSerializer(instance=user)

    return Response(data=serializer.data,status=status.HTTP_200_OK)





class ListNegociosForAuthor(generics.GenericAPIView,mixins.ListModelMixin):

    queryset=Negocio.objects.all()
    serializer_class=NegocioSerializer
    permission_classes =[IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        username=self.request.query_params.get("username") or None
        queryset=Negocio.objects.all()

        if username is not None:
            return Negocio.objects.filter(dueno__username__contains=username)
        
        return queryset

        

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


class ItemViewSet(viewsets.ModelViewSet):
    
    queryset = Item.objects.all()
    serializer_class= ItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['negocio__id','nuevo']










