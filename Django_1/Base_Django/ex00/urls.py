from django.urls import path 
from .views import Ex00

urlpatterns = [
    path('template/', Ex00.as_view())
]
