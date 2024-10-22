from django.urls import path
from . import views

urlpatterns = [
    path('', views.Init.as_view() , name='home')
]
