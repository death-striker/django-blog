from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import RegisterSerializer ,LoginSerializer



# Create your views here.

class RegisterUserView(APIView):
    permission_class = [AllowAny]
    def post(self, request):
        serializer= RegisterSerializer(data= request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "User Registered Successfully",
                "access_token": str(refresh.access_token),
                "refresh":str(refresh)
            },status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    permissionclasses = [AllowAny]
    def post(self,request):

        serializer= LoginSerializer(data=request.data)
        if serializer.is_valid():
            user= serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                "message":"User is authenticated",
                "access_token":str(refresh.access_token),
                "refresh_token":str(refresh)
            }, status = status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

