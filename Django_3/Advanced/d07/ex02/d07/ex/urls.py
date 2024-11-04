from django.urls import path
import ex.views

urlpatterns = [
    path('', ex.views.HomeView.as_view(), name='home'),
    path('login/', ex.views.Login.as_view(), name='login'),
    path('logout/', ex.views.Logout.as_view(), name='logout'),
    path('register/', ex.views.RegisterView.as_view(), name='register'),
    path('article/', ex.views.ArticlesView.as_view(), name='articles'),
    path('publish/', ex.views.PublishView.as_view(), name='publish'),
    path('article/<slug:pk>/', ex.views.DetailsView.as_view(), name='article'),
    path('publication/', ex.views.PublicationsView.as_view(), name='publication'),
    path('favourites/', ex.views.FavouritesView.as_view(), name='favourites'),
]
