from django.urls import path
from . import views
urlpatterns = [
    path('', views.Random.as_view() , name='')
]
