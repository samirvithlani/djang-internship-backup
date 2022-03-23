from django.contrib import admin
from django.urls import path
from society import views
from .views import CreateSociety

urlpatterns = [
    
    path("index/",views.index,name="index"),
    path("aboutus/",views.aboutUs,name="aboutUs"),
    path("contactus/",views.contactUs,name="contactUs"),
    path("createSociety/",CreateSociety.as_view(),name="createSociety"),
]
