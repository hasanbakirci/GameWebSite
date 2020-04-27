from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about' ),
    path('gamepage', views.gamepage, name='gamepage' ),
    path('registerindex', views.registerindex, name='registerindex' ),
    
    
   
]