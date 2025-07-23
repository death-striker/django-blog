from rest_framework import serializers
from .models import RegisterUser
from django.contrib.auth.password_validation import validate_password

# from django.contrib.auth import

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required = True,validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required = True)

    class Meta:
        model = RegisterUser
        fields = ['email','username','first_name','last_name','phone_number','address','password','password2']

    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password':'password didn\'t match'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = RegisterUser.objects.create_user(**validated_data)
        return user



