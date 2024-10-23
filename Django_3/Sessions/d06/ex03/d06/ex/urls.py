from django.urls import path
from ex.views import Init, VoteView, Register, Login, Logout

urlpatterns = [
    path('', Init.as_view() , name='home'),
    path('vote/<int:tip_id>/<str:vote_type>/', VoteView.as_view(), name='vote'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view() , name='login'),
    path('logout/', Logout.as_view() , name='logout')
]
