
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('posts.urls')), 
    path('api-auth/', include('rest_framework.urls')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),

    
]
