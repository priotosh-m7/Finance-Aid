"""mock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage', views.homepage, name="index"),
    path('SalaryCalculator/', include('SalaryCalculator.urls')),
    path('SalaryDetails/',include('SalaryCalculator.urls')),
    path('homeloan/', include('LoanCalculator.urls')),
    path('homeloandetails/', include('LoanCalculator.urls')),

    path("eduloan/", views.eduloan, name="eduloan"),
    path("eduloan/eduloandet/", views.eduloandet, name="eduloandet"),
    path('inflation/',include('InflationCalci.urls')),
    path('inflationdet/',include('InflationCalci.urls'))

    #    path('SalaryCalculator', views.SalaryCalculator, name="index3"),
#    path('SalaryDetails', views.SalaryDetails, name="SalaryDet")

]
