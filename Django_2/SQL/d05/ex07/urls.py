from django.urls import path
from . import views

urlpatterns = [
    path('populate/', views.Populate.as_view(), name='populate'),
    path('display/', views.Display.as_view(), name='display'),
    path('update/', views.Update.as_view(), name='update')
]