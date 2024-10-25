from django.urls import path
import ex.views 

urlpatterns = [
    path('', ex.views.Init.as_view() , name='home'),
    path('tip/', ex.views.TipView.as_view(), name='tip'),
    path('tip/delete/<int:id>', ex.views.DeleteTipView.as_view(), name='delete_tip'),
    path('tip/upvoted/<int:id>', ex.views.UpvotedTipView.as_view(), name='upvoted_tip'),
    path('tip/downvoted/<int:id>', ex.views.DownvotedTipView.as_view(), name='downvoted_tip'),
    path('register/', ex.views.Register.as_view(), name='register'),
    path('login/', ex.views.Login.as_view() , name='login'),
    path('logout/', ex.views.Logout.as_view() , name='logout')
]
