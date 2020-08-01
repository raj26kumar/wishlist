
from django.urls import path ,include
from . import views

urlpatterns = [

    path('', include('django.contrib.auth.urls')),
    #path('login', views.login, name="login"),
    path('login/register', views.register, name="register"),
    path('password_change/done/home2', views.home2, name="home2")
    

]
