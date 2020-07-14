from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!")

def index(request):
    return render(request,'AppOne/index.html')

def services(request):
    return render(request,'AppOne/services.html')

def contact(request):
    return render(request,'AppOne/contact.html')

def address(request):
    return render(request, 'AppOne/address.html')

def gallery(request):
    return render(request, 'AppOne/gallery.html')

def nosotros(request):
    return render(request, 'AppOne/nosotros.html')
