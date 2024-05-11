from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls', namespace='blog')),
    path('api/', include('blog_api.urls', namespace='blog_api')),
    path('auth/', include('accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls)
    
]
