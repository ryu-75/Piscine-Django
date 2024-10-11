from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.Init.as_view(), name='init')
]
