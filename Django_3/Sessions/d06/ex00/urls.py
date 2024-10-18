from django.urls import path
from . import views

urlpatterns = [
    path('', views.Init.as_view() , name=''),
    path('subscription/', views.Subscription.as_view(), name='subscription'),
    path('login/', views.Login.as_view() , name='login'),
    path('logout/', views.Logout.as_view() , name='logout'),
]
