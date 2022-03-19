from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def aboutUs(request):
    return render(request,'society/aboutUs.html')

def contactUs(request):
    return render(request,'society/contactUs.html')