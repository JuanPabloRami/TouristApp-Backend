from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    
    first_name = serializers.CharField(max_length = 60)
    last_name = serializers.CharField(max_length = 60)
    email = serializers.CharField(max_length = 80)
    username= serializers.CharField(max_length = 45)
    password = serializers.CharField(min_length = 8,write_only=True)
    
    class Meta:
        model = User
        fields= ['first_name','last_name','email','username','password']
        
    def validate(self, attrs):
        email_exists=User.objects.filter(email = attrs['email']).exists()
        username_exists=User.objects.filter(username = attrs['username']).exists()

        if email_exists:
            raise ValidationError("Error, Este correo ya esta en uso, intenta con otro.")

        if username_exists:
            raise ValidationError("Error, Este nombre de usuario ya esta en uso,intenta con otro")
        
        return super().validate(attrs)
    
    def create(self,validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)
        
        user.set_password(password)
        
        user.save()

        Token.objects.create(user=user)
        
        return user

