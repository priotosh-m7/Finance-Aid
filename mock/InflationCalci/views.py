from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages #import messages
from django.views.generic import TemplateView

import math

# Create your views here.

def inflationcalci(request):
    return render(request,"index6.html")

def inflationdet(request):

    P = float(request.GET.get('Principali'))
    N = float(request.GET.get('Tenurei'))
    R = float(request.GET.get('roii'))/100
    T = float(request.GET.get('roiis'))/100
    A =round( (P*math.pow((1+R),N)),2)
    ta = round((P*math.pow((1+T),N)),2)
    verdict = "Profit"
    res = 0
    if ta >= A:
        res = round((ta - A),2)
    else:
        verdict = "Loss"
        res = round((A- ta),2)
    params = {
        'P':P,"N":N,"R":R,"A":A,"t":ta , "ver":verdict,"res":res
    }
    return render(request,"infldet.html",params);
