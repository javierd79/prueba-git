from django.shortcuts import render

# Create your views here.

def indexPage(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'registro.html')

def login(request):
    return render(request, 'login.html')

def adminHome(request):
    return render(request, 'adminHome.html')