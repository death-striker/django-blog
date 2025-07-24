from django.urls import path
from .views import (RegisterUserView , LoginView ,BlogCreateView ,BlogPostListView,BlogPostDetailView,BlogPostUpdateDeleteView, UserProfileView, PublicUserProfileView, BlogPostsByUserView,MyBlogPostsView)
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name = 'register'),
    path('login/', LoginView.as_view(), name = 'login' ),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name = 'Profile-self'),

    path('posts/create/', BlogCreateView.as_view(), name ='create-post'),
    path('posts/', BlogPostListView.as_view(), name ="list-all-published-posts"),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name = 'post-details-published-by-id'),
    path('posts/<int:pk>/edit/', BlogPostUpdateDeleteView.as_view(), name='edit-post'),

    path('users/<int:user_id>/', PublicUserProfileView.as_view(), name='user-public-profile-by-user-id'),
    path('users/<int:user_id>/posts/', BlogPostsByUserView.as_view(), name='user-published-posts-by-user-id'),
    path('my-posts/', MyBlogPostsView.as_view(), name='my-posts-drafts'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)