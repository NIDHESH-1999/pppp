from django.db import models
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
User = get_user_model()
# Create your models here.
class TODO(models.Model):
    
    status_choices=[
        ("comp", "completed"),
        ("pend","PENDING"),
    ]
    st=[
        ("1", "1"),
        ("2","2"),
        ("3", "3"),
        ("4","4"), 
        ("5", "5"),
        ("6","6"), 
        ("7", "7"),
        ("8","8"),
    ]
    id=models.IntegerField(primary_key=True)
    Title=models.CharField(max_length=30)
    Status=models.CharField(max_length=9 ,
    choices= status_choices,default='Pend')
    Date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='1')
    
    Priority=models.CharField(max_length=2 ,
    choices= st,default='1')
def __str__(self):
    		return self.user
