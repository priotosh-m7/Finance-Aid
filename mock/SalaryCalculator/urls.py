from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.SalaryCalculator,name="InputDetails"),
    path("SalaryDetails/", views.SalaryDetails, name="details"),


]


