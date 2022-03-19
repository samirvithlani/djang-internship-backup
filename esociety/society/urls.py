from django.contrib import admin
from django.urls import path
from society import views

urlpatterns = [
    
    path("index/",views.index,name="index"),
    path("aboutus/",views.aboutUs,name="aboutUs"),
    path("contactus/",views.contactUs,name="contactUs"),
]
