from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import RegisterUser , BlogPost
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

class LoginSerializer(serializers.Serializer):

    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)

    def validate(self,attrs):
        email=attrs.get('email')
        password=attrs.get('password')

        if email and password:
            user=authenticate(request=self.context.get('request'), email=email,password=password)
            if not user:
                raise serializers.ValidationError("Invalid email or password.")
        else:
            raise serializers.ValidationError("Both email and password are required.")

        attrs['user'] = user
        return attrs

class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    class Meta:
        model=BlogPost
        fields='__all__'
        read_only_fields=['id','author','created_at','updated_at']

class ProfileViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegisterUser
        fields = ['username', 'email', 'id', 'first_name', 'last_name', 'phone_number', 'address', 'avatar']
        read_only_fields = [ 'id', 'email',' username']

class PublicUserSerializer (serializers.ModelSerializer):

    class Meta:

        model = RegisterUser
        fields = [ 'id', 'username', 'email', 'first_name', 'last_name' ]
