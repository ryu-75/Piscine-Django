from django.urls import path
import ex.views

urlpatterns = [
    path('', ex.views.HomeView.as_view(), name='home'),
    path('register/', ex.views.Register.as_view(), name='register'),
    path('login/', ex.views.Login.as_view(), name='login'),
    path('logout/', ex.views.Logout.as_view(), name='logout'),
    path('article/', ex.views.ArticlesView.as_view(), name='article'),
    path('publication/', ex.views.PublicationsView.as_view(), name='publication'),
    path('favourites/', ex.views.FavouritesView.as_view(), name='favourites'),
    path('details/', ex.views.DetailsView.as_view(), name='details'),
    path('details/<int:id>/', ex.views.DetailsView.as_view(), name='details'),
]