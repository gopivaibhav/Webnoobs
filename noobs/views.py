from django.shortcuts import render
from .forms import Queryform

def home(request):
    form=Queryform()
    if request.method=='POST':
        form=Queryform(request.POST)
        if form.is_valid():
            form.save()        

    return render(request,'index.html',{'form':form})

def new(request):
    par={'tc':100,'nc':40,'rc':20,'de':10}
    return render(request,'corona.html',par)


