from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',                include('base.urls')),
    path('admin/',          admin.site.urls),
    path('api/users/',      include('base.urls.user_urls')),
    path('api/creators/',   include('base.urls.creator_urls')),
    path('api/projects/',   include('base.urls.project_urls')),
]