from django.urls import path
from views import home_page_view

urlpatterns = [
    path('helloword', home_page_view),
]
