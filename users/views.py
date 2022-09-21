from cgitb import reset
from urllib import response
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from .tokens import create_jwt_pair_for_user

from .serializers import SignUpSerializer
# Create your views here.

# @api_view(http_method_names=["GET","POST"])
# def home(request:Request):

#     if request.method == "POST":
#         data = request.data
#         response = {"mensaje":"hola mundo pero en rest f" ,"datos": data }
#         return Response(data = response, status = status.HTTP_201_CREATED)
#     response = {"mensaje":"hola mundo pero en rest f"}
#     return Response(data = response, status = status.HTTP_200_OK)

class signUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []
    
    def post(self,request:Request):
        data = request.data
        
        serializer = self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save()
            
            response = {
                "message":"Usuario creado correctamente",
                "data":serializer.data
            }
            return Response(data = response,status = status.HTTP_201_CREATED)
        return Response(data = serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):

    permission_classes = []
    def post(self,request:Request):


        email = request.data.get('email')
        password = request.data.get('password')
        
        user=authenticate(email=email,password = password)
        
        if user is not None:

            tokens = create_jwt_pair_for_user(user)
            response = {
                "message":"Se ha logueado con exito",
                "tokens":tokens
            }
            
            return Response(data=response,status=status.HTTP_200_OK)
        data = {
            "message":"Email o password invalido"
            }
        return Response(data=data)
    
    
    def get(self,request:Request):
        content={
            "user":str(request.user),
            "auth":str(request.auth)
        }

        return Response(data=content,status=status.HTTP_200_OK)

