from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.homeloan,name="homeloan"),
    path("homeloandet/",views.homeloandet,name="homeloandet"),



    #path("SalaryDetails/", views.SalaryDetails, name="details"),


]