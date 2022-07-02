
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages #import messages
from django.views.generic import TemplateView




def SalaryCalculator(request):
    return render(request, 'index3.html')

# Create your views here.

def SalaryDetails(request):

    ctc = float(request.GET.get('inputctc'))
    bonus = float(request.GET.get('bonus'))
    bonustype = request.GET.get('bonustype')
    total_bonus = 0
    if bonustype == 'percent':
        total_bonus = (bonus*ctc)*0.01
    elif bonustype == 'amt':
        total_bonus = bonus
    else:
        total_bonus = 0

    total_salary = ctc-total_bonus



    basic_salary = .5*total_salary
    #da = float(request.GET.get('dall'))

    epf = float(request.GET.get('epf'))
    experience = float(request.GET.get('exp'))
    annual_epf = 12*epf
    gratuity = ((basic_salary)/12)*(0.58)*experience
    location = request.GET.get('loc')
    prof_tax = 12*float(request.GET.get('pftax'))
    pf = float(request.GET.get('epf'))
    insurance = 12*float(request.GET.get('einsurance'))
    additional1 = float(request.GET.get('Add1'))
    additional2 = float(request.GET.get('Add2'))
    additional3 = float(request.GET.get('Add3'))
    additional1dur = request.GET.get('add1dur')
    additional2dur = request.GET.get('add2dur')
    additional3dur = request.GET.get('add3dur')
    if additional1dur=='monthly':
        additional1 = additional1*12
    if additional2dur=='monthly':
        additional2 = additional2*12
    if additional3dur=='monthly':
        additional3 = additional3*12
    hra = 0
    if location=='metro':
        hra = 0.5*basic_salary
    else:
        hra = 0.4*basic_salary



    total_deductions = prof_tax+(2*annual_epf)+insurance+additional1+additional2+additional3
    gross_salary = ctc - annual_epf - gratuity
    taxable_income = total_salary-total_deductions

    it = 0
    cess = 0.04*taxable_income
    if taxable_income > 250000 and taxable_income<= 500000:
        it = 0.05*taxable_income
    elif taxable_income>500000 and taxable_income<=1000000:
        it = 12500+ 0.2*(taxable_income-500000)
    else:

        it = 112500 + 0.3*(taxable_income-1000000)

    inhandsal = taxable_income-it
    ihspm = round((inhandsal/12),2)
    takehome_salary = round((inhandsal)/12)

    additional = round(additional2+additional3+additional1)

    params = {'CTC':ctc,'Gross':gross_salary,'taxable':taxable_income,'tbonus':total_bonus,
              'bs':basic_salary,'ins':insurance,
              'hra':hra,'ad':additional,'ad1':additional1,'ad2':additional2,'ad3':additional3,'it':it,'ihs':inhandsal,'ihspm':ihspm,
              'epf':annual_epf,'gt':gratuity,'prof':prof_tax,'res':takehome_salary, 'ts':total_salary , 'td':total_deductions
              }

    return render(request,'salarydetails.html',params)
