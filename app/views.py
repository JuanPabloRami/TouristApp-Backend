
from django.shortcuts import render,redirect, get_object_or_404
from rest_framework import status, viewsets, generics,mixins
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import APIView,api_view, permission_classes

from .models import Tipo_Negocio,Negocio,Item
from .serializers import TipoSerializer,NegocioSerializer,ItemSerializer
from rest_framework.permissions import IsAuthenticated
from users.serializers import CurrentUserNegocioSerializer

# Create your views here.


class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo_Negocio.objects.all()
    serializer_class= TipoSerializer
    permission_classes = [IsAuthenticated]

# class NegocioViewSet(viewsets.ModelViewSet):

#     queryset = Negocio.objects.all()
#     serializer_class= NegocioSerializer
#     permission_classes = [IsAuthenticated]

# class NegocioListAndCreateView(APIView):
#     serializer_class=NegocioSerializer
#     permission_classes = [IsAuthenticated]
#     def get(self,request:Request,*args,**kwargs):
        
#         negocio = Negocio.objects.all()
#         serializer = self.serializer_class(instance=negocio,many=True)
#         return Response(data=serializer.data,status = status.HTTP_200_OK)

#     def post(self,request:Request,*args,**kwargs):
#         data = request.data
#         serializer=self.serializer_class(data=data)
        
#         if serializer.is_valid():
            
#             serializer.save()
#             response = {
#                 "Message":"Negocio creado correctamente",
#                 "data":serializer.data
#             }

#             return Response(data=response,status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class NegocioRetrieveUpdateDeleteView(APIView):
#     serializer_class = NegocioSerializer

#     def get(self,request:Request,id_negocio:int):
#         negocio = get_object_or_404(Negocio,pk=id_negocio)

#         serializer=self.serializer_class(instance=negocio)

#         return Response(data=serializer.data,status=status.HTTP_200_OK)

#     def put(self,request:Request,id_negocio:int):
#         negocio = get_object_or_404(Negocio,pk=id_negocio)
#         data=request.data
#         serializer = self.serializer_class(instance=negocio,data=data)
        
#         if serializer.is_valid():
#             serializer.save()

#             response={
#                 "message":"negocio editado correctamente",
#                 "data":serializer.data
#             }

#             return Response(data=response,status=status.HTTP_200_OK)
#         return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request:Request,id_negocio:int):
#         negocio = get_object_or_404(Negocio,pk=id_negocio)

#         negocio.delete()

#         response = {
#             "message":"Negocio Eliminado correctamente"
#         }

#         return Response(data=response,status=status.HTTP_204_NO_CONTENT)
        

class NegocioListAndCreateView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class= NegocioSerializer
    queryset=Negocio.objects.all()

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




class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class= ItemSerializer
    permission_classes = [IsAuthenticated]







