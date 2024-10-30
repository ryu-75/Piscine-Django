from django.urls import path
import ex.views

urlpatterns = [
    path('', ex.views.HomeView.as_view(), name='home'),
    path('login/', ex.views.Login.as_view(), name='login'),
    path('article/', ex.views.ArticlesView.as_view(), name='article'),
]
