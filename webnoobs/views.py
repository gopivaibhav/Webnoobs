from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def new(request):
    par={'tc':100,'nc':40,'rc':20,'de':10}
    return render(request,'corona.html',par)