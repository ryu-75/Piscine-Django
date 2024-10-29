from django.urls import path
import ex.views

urlpatterns = [
    path('', ex.views.Home.as_view(), name='home'),
    path('register/', ex.views.Register.as_view(), name='register'),
    path('login/', ex.views.Login.as_view(), name='login'),
    path('logout/', ex.views.Logout.as_view(), name='logout'),
]
