from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('ranking', views.ranking, name='ranking'),
    path('ranking_main', views.ranking_main, name='ranking_main'),


]