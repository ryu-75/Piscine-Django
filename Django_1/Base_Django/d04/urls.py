from django.contrib import admin
from django.urls import path
from ex00.views import ex00
from ex01.views import html_render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ex00/index', ex00),
    path('ex01/<slug:slug>/', html_render, name="ex01"),
]
