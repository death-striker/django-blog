
from .serializer import RegisterSerializer ,LoginSerializer ,BlogPostSerializer , ProfileViewSerializer ,PublicUserSerializer
from .models import BlogPost , RegisterUser
from django.db.models import Q

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny , IsAuthenticated



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
    permission_classes = [AllowAny]
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

class BlogCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):

        serializer = BlogPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(author = request.user)
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response (serializer.errors, status = status.HTTP_400_BAD_RESPONSE)


class BlogPostListView(APIView):
    permission_classes= [AllowAny]

    def get(self, request):
        query = request.GET.get('search', '')
        posts = BlogPost.objects.filter(
                Q(is_published=True) & (
                Q(title__icontains=query) | Q(content__icontains=query))
).order_by('created_at')
        paginator=PageNumberPagination()
        paginated_posts=paginator.paginate_queryset(posts,request)
        serializer= BlogPostSerializer(paginated_posts,many=True)
        return paginator.get_paginated_response(serializer.data)

class BlogPostDetailView(APIView):
    permissionclasses = [AllowAny]

    def get(self, request,pk):
        try:
            post = BlogPost.objects.get(pk = pk,is_published=True)
        except BlogPost.DoesNotExist:
            return Response({'Error': "Post Not found"}, status= 404)

        serializer =BlogPostSerializer(post)
        return Response(serializer.data)

class BlogPostUpdateDeleteView(APIView):

    permission_classes = [IsAuthenticated]

    def put(self,request,pk):
        try :
            post = BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            return Response({'error': "Blog Post does not exists"}, status = status.HTTP_400_BAD_REQUEST)

        if post.author != request.user:
            raise PermissionError("Unauthorised Access")

        serializer = BlogPostSerializer(post , data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = 400)

    def delete(self, request,pk):
        try :
            post= BlogPost.objects.get(pk = pk)
        except BlogPost.DoesNotExist:
            return Response({'error': 'Blog Post does not exist'}, status = status.HTTP_400_BAD_REQUEST)

        if post.author!= request.user:
            raise PermissionError('Unauthorized access')
        post.delete()
        return Response({"Delete": "Post has been successfully deleted"}, status = 204)


class UserProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileViewSerializer(request.user)
        return Response(serializer.data)

    def put (self, request):

        serializer = ProfileViewSerializer ( request.user , data = request.data, partial = True )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = 400)

class PublicUserProfileView(APIView):
    permission_classes = [AllowAny]
    def get(self,request, user_id):

        try:
            user = RegisterUser.objects.get(id = user_id)
        except RegisterUser.DoesNotExist:
            return Response({"Error": "User not found"}, status = status.HTTP_400_BAD_REQUEST)

        serializer = PublicUserSerializer(user)
        return Response(serializer.data)


class BlogPostsByUserView(APIView):
    permisssion_classes = [AllowAny]

    def get(self,request,user_id):
            post= BlogPost.objects.filter(author_id = user_id).order_by('-created_at')
            serializer = BlogPostSerializer(post, many=True)
            return Response(serializer.data)



class MyBlogPostsView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request):
        posts = BlogPost.objects.filter(author= request.user).order_by('-created_at')
        serializer = BlogPostSerializer(posts, many=True)
        return Response(serializer.data)


