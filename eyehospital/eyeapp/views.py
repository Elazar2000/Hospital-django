from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse("")
def home(request):
    name = 'Hospital'
    return render(request, 'home.html',{'obj': name})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def thank(request):
    return render(request, 'thank.html')

def detail(request):
    return HttpResponse('At our eye hospital, we specialize in diagnosing and treating a wide range of eye conditions')