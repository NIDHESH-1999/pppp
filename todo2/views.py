from django.shortcuts import render,redirect
from .forms import TODOFORM
from .models import TODO

# Create your views here.

def home(request):
    form=TODOFORM()
    todos=TODO.objects.filter(user=request.user)
    

    return render(request,"home.html",context={"form":form,"todos":todos})
def todo6(request):
    if request.user.is_authenticated:
     user=request.user

     form=TODOFORM(request.POST)
     print(user)
     if form.is_valid():
        print(form.cleaned_data)

        
        todo = form.save(commit=False)
     
        todo.user=user
        todo.save()
        print(user)
        return redirect("home")
    
     else:
        return render(request,"index.html",context={"form":form})
