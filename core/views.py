from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "core/home.html")

def portafolio(request):
    return render(request, "core/portafolio.html")

def cv(request):
    return render(request, "core/cv.html")

def contacto(request):
    return render(request, "core/contacto.html")

# Create your views here.
