from django.urls import path
from . import views

#insert urls of our homescreen app

urlpatterns = [
    path('', views.home, name = 'home-screen'),   #url for our home view(path,location,name) ->epistrefei th synarthsh views.home
    path('about/', views.about, name = 'home-about'),
]