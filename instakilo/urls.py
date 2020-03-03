from django.contrib import admin
from django.urls import path
from .import views
urlpatterns= [
path('home', views.home, name="n1"),
path('login', views.login, name="n2"),
path('common', views.common, name="n3"),
path('main', views.main, name="n4"),
path('logout', views.logout, name="n5"),
path('profile', views.profile, name="n6"),
]