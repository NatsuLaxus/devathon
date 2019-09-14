from django.urls import path

from . import views

urlpatterns = [

	path('',views.index),
	path('inside/',views.inside),
	path('register_new/',views.register_new)
]