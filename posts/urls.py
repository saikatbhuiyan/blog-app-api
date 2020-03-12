from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PostListCreate, PostDetail, UserDetail, UserList, some_view, UserViewSet, PostViewSet

router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('', PostViewSet, base_name='posts')

urlpatterns = [
  path('router/', include(router.urls)),
  path('', PostListCreate.as_view()),
  path('<int:pk>/', PostDetail.as_view()),
  path('lab/', some_view, name='lab'),
  path('users/', UserList.as_view()), 
  path('users/<int:pk>/', UserDetail.as_view()), 
  
]