from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.inflationcalci,name="infi"),
    path("inflationdet/",views.inflationdet,name="inflationdet"),



    #path("SalaryDetails/", views.SalaryDetails, name="details"),


]