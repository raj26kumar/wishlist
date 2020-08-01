from django import forms
from django.contrib.auth.models import User 
from .models import List



class ListForm(forms.ModelForm):
    class Meta :
        model = List
        fields = [  "item",
                    "date",  ]
 

