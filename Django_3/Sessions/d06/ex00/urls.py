from django.urls import path
from . import views
urlpatterns = [
    path('', views.Init.as_view() , name=''),
    path('subscription/', views.Subscription.as_view(), name='subscription'),
    path('connexion/', views.Connexion.as_view() , name='connexion')
]
