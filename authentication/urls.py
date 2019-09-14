from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login_page),
    path('register/', views.register),
    path('home/', views.index),
    path('logout/', views.logout_page),
]