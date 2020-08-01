from django.db import models
from datetime import datetime, date
from django.db.models import Model
from django.contrib.auth.models import User


# Create your models here.
class List(models.Model):
    item = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=False, auto_now= False , blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def datepublished(self):
        return self.published_date.strftime('%B %d %Y')

    def __str__(self):
        return self.item 


