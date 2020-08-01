from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name="base"),                     #for base
    path('home', views.home, name="home"),                 #after login
    path('delete/<list_id>', views.delete, name="delete"), #when u delete
    
    
   
    
]