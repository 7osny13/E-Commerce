from email import message
from django.shortcuts import render
from django.http import JsonResponse
# from .products import products
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
# from .models import Product
from base.serializers import ProductSerializer,userSerializer,UserSerilezerwithToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status



# -------------------------------------------JWT Custmizer -----------------------------------------------------
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
 

    def validate(self, attrs):
        data = super().validate(attrs)
        serializers=UserSerilezerwithToken(self.user).data
        for k,v in serializers.items():
            data[k]= v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
#----------------------------------------------
#-----register user-------------------

@api_view(['POST'])
def registerUser(request):
  
    data=request.data
    print('Data',data)
    try:
        user=User.objects.create(
            first_name= data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])

        )
        serializer=UserSerilezerwithToken(user,many=False)
        return Response(serializer.data)
    except:
        message= {'detail':'user with this email is already exist'}
        return Response(message,status=status.HTTP_400_BAD_REQUEST)

def getRoutes(request):
    return JsonResponse("Hello",safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserprofile(request):
    user=request.user
    
    serializer= userSerializer(user , many=False)
    return Response(serializer.data )
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getusers(request):
    users = User.objects.all()
    serializer= userSerializer(users , many=True)
    return Response(serializer.data )

