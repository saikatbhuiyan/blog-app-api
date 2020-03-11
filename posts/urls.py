from django.urls import path,
from .views import PostListCreate, PostDetail, UserDetail, UserList


urlpatterns = [
  path('', PostListCreate.as_view()),
  path('<int:pk>/', PostDetail.as_view()),
  path('users/', UserList.as_view()), 
  path('users/<int:pk>/', UserDetail.as_view()), 
]