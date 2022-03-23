from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Society,Flats

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def aboutUs(request):
    return render(request,'society/aboutUs.html')

def contactUs(request):
    return render(request,'society/contactUs.html')


class CreateSociety(CreateView):
    model = Society
    fields = ['name','description','address','city','state','zipcode','year']
    template_name = 'society/createSociety.html'
    success_url = 'society/index/'
