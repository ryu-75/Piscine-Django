from django.contrib import admin
from django.urls import path
from django.urls.conf import include 

urlpatterns = [
    path('ex00/', include('ex00.urls')),
    path('ex01/', include('ex01.urls')),
    path('ex02/', include('ex02.urls')),
    path('ex03/', include('ex03.urls')),
    path('admin/', admin.site.urls),
]
