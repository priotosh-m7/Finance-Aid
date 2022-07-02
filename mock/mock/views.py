from django.http import HttpResponse
from django.shortcuts import render

import math

def homepage(request):
    return render(request, 'index2.html')

def eduloan(request):
    return render(request,'index5.html')

def eduloandet(request):

    P = float(request.GET.get('Principale'))
    N = float(request.GET.get('Tenuree'))
    re = float(request.GET.get('roie'))
    R = re/12/100
    n = N/12

    EMI = round((P * R * math.pow(1 + R, N)) / ((math.pow(1 + R, N - 1)) - 1), 2)
    te = EMI*N
    tot = round(P+te,2)

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
        "P": P, "N": N, "R": R, "EMI": EMI, "n":n, "re":re, "te":te, "tot":tot,
        "kotak": kot_emi,

        "BankofBaroda": bob_emi,

        "SBI": sbi_emi,
        "HDFC": hdfc_emi,
        "AxisBank": axis_emi,

    }

    return render(request, 'eduloandetails.html', params)





"""
def SalaryCalculator(request):
    return render(request, 'index3.html')

def SimpleInterest(request):
    P = int(request.GET.get('Princi','0'))
    R = int(request.GET.get('rate','4'))
    N = int(request.GET.get('period','4'))
    SI = (P*R*N)/100
    params = {'principal':P,'rate':R,'period':N,'interest':SI}
    return render(request,'simpleinterest.html',params)

def SalaryDetails(request):

    ctc = float(request.GET.get('inputctc'))
    basic_salary = .5*ctc
    da = float(request.GET.get('dall'))
    Dearance_Allowance = (da*0.01)*basic_salary
    epf = float(request.GET.get('epf'))
    experience = float(request.GET.get('exp'))
    annual_epf = 12*epf
    gratuity = ((basic_salary+Dearance_Allowance)/12)*(0.58)*experience
    location = request.GET.get('loc')
    prof_tax = float(request.GET.get('pftax'))
    pf = float(request.GET.get('epf'))
    insurance = float(request.GET.get('einsurance'))
    additional1 = float(request.GET.get('Add1'))
    additional2 = float(request.GET.get('Add2'))
    additional3 = float(request.GET.get('Add3'))
    additional1dur = request.GET.get('add1dur')
    additional2dur = request.GET.get('add2dur')
    additional3dur = request.GET.get('add3dur')
    if additional1dur=='yearly':
        additional1=additional1*12
    if additional2dur=='yearly':
        additional2=additional2*12
    if additional3dur=='yearly':
        additional3=additional3*12
    hra = 0
    if location=='metro':
        hra = 0.5*basic_salary
    else:
        hra = 0.4*basic_salary
    gross_salary = ctc - annual_epf - gratuity
    taxable_income = gross_salary-prof_tax-pf-insurance-additional1-additional2-additional3-hra

    params = {'CTC':ctc,'Gross':gross_salary,'taxable':taxable_income}
"""
#    return render(request,'salarydetails.html',params)
