from django.urls import path
import account.views as views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='index.html', next_page='login'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)