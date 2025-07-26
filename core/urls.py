from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.api.urls')),  
    path('api/content/', include('content.api.urls')),
]

