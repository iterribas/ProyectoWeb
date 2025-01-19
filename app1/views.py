from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")

def servicios(request):
    return render (request, "services.html")

def tienda(request):
    return HttpResponse('tienda')

def blog(request):
    return render(request, 'blog.html')
    
def contacto(request):
    return render (request, 'contacto.html')

def base(request):
    return render (request,'base.html')


# Create your views here.
