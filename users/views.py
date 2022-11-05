from cgitb import reset
from urllib import response
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from .tokens import create_jwt_pair_for_user
from .models import User

from .serializers import SignUpSerializer,ResetPwEmailSerializer
# Create your views here.

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str,smart_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import  get_current_site
from django.urls import reverse
from .utils import Util

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
        return Response(data=data,status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self,request:Request):
        content={
            "user":str(request.user),
            "auth":str(request.auth)
        }

        return Response(data=content,status=status.HTTP_200_OK)

class RequestResetPwEmailView(generics.GenericAPIView):
    serializer_class = ResetPwEmailSerializer
    permission_classes =[]
    def post(self,request):
        # data = {'request':request,'data':request.data}
        serializer = self.serializer_class(data=request.data)
        # serializer.is_valid(raise_exception=True)
        email = request.data['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64=urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)

            current_site = get_current_site(request = request).domain
            relativeLink = reverse('password-reset-confirm',kwargs={'uidb64':uidb64,'token':token})
            absurl='http://'+current_site+relativeLink+"?token="+str(token)
            email_body = "hola \n verifica tu email en touristapp para que puedas restrablecer tu contraseña usando el siguiente link \n"+absurl
            data = {
                'email_body':email_body,
                'to_email':user.email,
                'email_subject':'[Touristapp] restablece tu contraseña'
                }

            Util.send_mail(data)
            return Response({'success':'Te hemos enviado un correo de confirmacion para restablecer tu contraseña.'},status=status.HTTP_200_OK)
        return Response({'dolor':'no se envio ni chimba'},status=status.HTTP_403_FORBIDDEN)

class PasswordTokenCheckView(generics.GenericAPIView):
    def get(self,request,uidb64,token):
        pass