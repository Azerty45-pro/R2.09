from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('index/', views.index),
    path('formulaire/', views.formulaire),
    path('bonjour/', views.bonjour),

]