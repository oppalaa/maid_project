from django.shortcuts import render

# Create your views here.

def User_login(request):
    
    return render(request,'User_login.html')

def home(request):
    return render(request,'home.html')

def services(request):
    return render(request,'services.html')
