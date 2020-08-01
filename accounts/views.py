from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    #email= request.POST.get('email')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", { 'form':form, })               
    
 #<!-- go check setting.py to see login /logout urls -->

def home2(request):
    return redirect('login')