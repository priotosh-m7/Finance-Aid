
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages #import messages
from django.views.generic import TemplateView

import math



def homeloan(request):
    return render(request,'index4.html')

def eduloan(request):
    return render(request,'index5.html')


def homeloandet(request):

    roi = {
        "kotak": 6.55,
        "citi":6.75,
        "Bank of Baroda":6.60,
        "CenBOI":6.85,
        "SBI":6.75,
        "HDFC":6.75,
        "Axis Bank":6.90,
        "IDBI":6.75,
        "DHFL":8.75

    }

    r = [0.0655,0.0675,0.0660,0.0685,0.0675,0.0675,0.0690,0.0675,0.0875]

    emis = [0,1]

    P = float(request.GET.get('Principal'))
    N = float(request.GET.get('Tenure'))
    re = float(request.GET.get('roi'))
    n = N/12
    R = re/12/100
    EMI = round((P*R*math.pow(1+R,N))/((math.pow(1+R,N-1))-1),2)
    te = EMI*N

    tot = P+te

   # for i in r:
    kot_emi = round((P*r[0]*math.pow(1+r[0],N))/((math.pow(1+r[0],N-1))-1),2)
    citi_emi = round((P * r[1] * math.pow(1 + r[1], N)) / ((math.pow(1 + r[1], N - 1)) - 1), 2)
    bob_emi = round((P * r[2] * math.pow(1 + r[2], N)) / ((math.pow(1 + r[2], N - 1)) - 1), 2)
    #kot_emi = round((P * r[3] * math.pow(1 + r[0], N)) / ((math.pow(1 + r[0], N - 1)) - 1), 2)
    cbi_emi = round((P * r[3] * math.pow(1 + r[3], N)) / ((math.pow(1 + r[3], N - 1)) - 1), 2)
    sbi_emi = round((P * r[4] * math.pow(1 + r[4], N)) / ((math.pow(1 + r[4], N - 1)) - 1), 2)
    hdfc_emi = round((P * r[5] * math.pow(1 + r[5], N)) / ((math.pow(1 + r[5], N - 1)) - 1), 2)
    axis_emi = round((P * r[6] * math.pow(1 + r[6], N)) / ((math.pow(1 + r[6], N - 1)) - 1), 2)
    idbi_emi = round((P * r[7] * math.pow(1 + r[7], N)) / ((math.pow(1 + r[7], N - 1)) - 1), 2)
    dhfl_emi = round((P * r[8] * math.pow(1 + r[8], N)) / ((math.pow(1 + r[8], N - 1)) - 1), 2)





    params = {
        "P":P, "N":N , "R":R, "EMI":EMI, "re":re,"n":n,"te":te,"tot":tot,
        "kotak": kot_emi,
        "citi": citi_emi,
        "BankofBaroda": bob_emi,
        "CenBOI": cbi_emi,
        "SBI": sbi_emi,
        "HDFC": hdfc_emi,
        "AxisBank": axis_emi,
        "IDBI": idbi_emi,
        "DHFL": dhfl_emi
              }

    return render(request,'homeloandetails.html',params)



def eduloandet(request):


    P = float(request.GET.get('Principale'))
    N = float(request.GET.get('Tenuree')) * 12
    R = float(request.GET.get('roie')) / 12 / 100
    n = N/12
    r = R*12*100

    EMI = round((P * R * math.pow(1 + R, N)) / ((math.pow(1 + R, N - 1)) - 1), 2)
    e = EMI*N

    # for i in r:
    kot_emi = round((P * (0.1150/12) * math.pow(1 + (0.1150/12), N)) / ((math.pow(1 + (0.1150/12), N - 1)) - 1), 2)

    axis_emi = round((P * (0.1150 / 12) * math.pow(1 + (0.1150 / 12), N)) / ((math.pow(1 + (0.1150 / 12), N - 1)) - 1),
                    2)

    if P<=400000:
        axis_emi = round((P * (0.1520/12) * math.pow(1 + (0.1520/12), N)) / ((math.pow(1 + (0.1520/12), N - 1)) - 1), 2)
    elif P>400000 and P<=750000:
        axis_emi = round((P * (0.1470/12) * math.pow(1 + (0.1470/12), N)) / ((math.pow(1 + (0.1470/12), N - 1)) - 1), 2)
    else:
        axis_emi = round((P * (0.1370/12) * math.pow(1 + (0.1370/12), N)) / ((math.pow(1 + (0.1370/12), N - 1)) - 1), 2)



    #citi_emi = round((P * r[1] * math.pow(1 + r[1], N)) / ((math.pow(1 + r[1], N - 1)) - 1), 2)
    bob_emi = round((P * (0.0850/12) * math.pow(1 + (0.0850/12), N)) / ((math.pow(1 + (0.0850/12), N - 1)) - 1), 2)

    # kot_emi = round((P * r[3] * math.pow(1 + r[0], N)) / ((math.pow(1 + r[0], N - 1)) - 1), 2)
    can_emi = 0# round((P * r[3] * math.pow(1 + r[3], N)) / ((math.pow(1 + r[3], N - 1)) - 1), 2)
    if P <= 400000:
        can_emi = round(
            (P * (0.1040 / 12) * math.pow(1 + (0.1040 / 12), N)) / ((math.pow(1 + (0.1040 / 12), N - 1)) - 1), 2)
    elif P > 400000 and P <= 750000:
        can_emi = round(
            (P * (0.1040 / 12) * math.pow(1 + (0.1040 / 12), N)) / ((math.pow(1 + (0.1040 / 12), N - 1)) - 1), 2)
    else:
        can_emi = round(
            (P * (0.1020 / 12) * math.pow(1 + (0.1020 / 12), N)) / ((math.pow(1 + (0.1020 / 12), N - 1)) - 1), 2)


    sbi_emi = 0# round((P * r[4] * math.pow(1 + r[4], N)) / ((math.pow(1 + r[4], N - 1)) - 1), 2)

    if P<=750000:
        sbi_emi = round((P * (0.1025 / 12) * math.pow(1 + (0.1025 / 12), N)) / ((math.pow(1 + (0.1025 / 12), N - 1)) - 1), 2)
    else:
        sbi_emi = round(
            (P * (0.1050 / 12) * math.pow(1 + (0.1050 / 12), N)) / ((math.pow(1 + (0.1050 / 12), N - 1)) - 1), 2)


    hdfc_emi = round((P * (0.09/12) * math.pow(1 + (0.09/12), N)) / ((math.pow(1 + (0.09/12), N - 1)) - 1), 2)


    params = {
        "P": P, "N": N, "R": R, "EMI": EMI, "n":n, "r":r, "e":e,
        "kotak": kot_emi,

        "BankofBaroda": bob_emi,

        "SBI": sbi_emi,
        "HDFC": hdfc_emi,
        "AxisBank": axis_emi,

    }

    return render(request, 'eduloandetails.html', params)


# Create your views here.
