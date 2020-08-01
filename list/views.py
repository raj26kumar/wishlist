from django.shortcuts import render , redirect ,reverse
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User





# Create your views here.





def base(request):             
    return render(request ,'base.html')


@login_required
def home(request):
    item = request.POST.get('item')
    date = request.POST.get('date')
    
    if item=="":
        messages.error(request, "Type something in your wish-list")
        #all_items = List.objects.all
        all_items = List.objects.filter(owner=request.user)
        return render(request,'home.html',{'all_items': all_items}) 

    elif date=="" :
        messages.error(request, "select date")
        #all_items = List.objects.all
        all_items = List.objects.filter(owner=request.user)
        return render(request,'home.html',{'all_items': all_items})   

    else:

        if request.method == 'POST':
            form = ListForm(request.POST or None)    # <!-- here we are assigns listform to a variable 'form' -->

            if form.is_valid():
                if User.is_authenticated:
                    all_items = List.objects.filter(owner=request.user)
                    new_topic = form.save(commit=False)
                    new_topic.owner = request.user
                    new_topic.save()
                    
                    return render(request, 'home.html', {'all_items': all_items})

                """ else:
                    
                    all_items = List.objects.filter(owner=false)   # <!-- here we are sending user input(models list) as output and displaying  -->
                    form.save()
                    messages.success(request, ('Added to Wish List '))
                    return render(request, 'home.html', {'all_items': all_items})"""
                
        else:
            #all_items = List.objects.all
            all_items = List.objects.filter(owner=request.user)
            return render(request,'home.html',{'all_items': all_items})       

    
       

def delete(request, list_id):
    item = List.objects.get(pk=list_id)   # <!-- here we are getting particlar item and its date(all related to it) -->
    item.delete()
    messages.success(request, ('Item deleted'))
    return redirect('home')




