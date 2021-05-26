from django.shortcuts import render
from .models import Query
def home(request):      
    if request.method=="POST":
        Name=request.POST.get('Name', '')
        Email=request.POST.get('Email', '')
        Message=request.POST.get('Message', '')
        
        hello=Query(Name=Name,Email=Email,Message=Message)
        hello.save()
    return render(request,'index.html')

def new(request):
    par={'tc':100,'nc':40,'rc':20,'de':10}
    return render(request,'corona.html',par)


