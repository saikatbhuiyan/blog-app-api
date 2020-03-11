from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

class PostListCreate(generics.ListCreateAPIView):
  """Post list and create api view."""
  permission_class = (permissions.IsAuthenticated)
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  """Post retrieve update and destroy api view."""
  permission_classes = (IsAuthorOrReadOnly,)
  queryset = Post.objects.all()
  serializer_class = PostSerializer



class UserList(generics.ListCreateAPIView): 
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateAPIView):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer

class UserViewset(viewsets.ModelViewSet):
  """Use viewsets for user create, update, list, retrive"""
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer
