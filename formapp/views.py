from django.shortcuts import render
from django.http import HttpResponse
from .forms import FillDetails,Log
from .models import Students

# Create your views here.

def Index(request):
    if request.method=='POST':
        gf=FillDetails(request.POST)
        if gf.is_valid():
            # print(gf.cleaned_data['name'])
            # s=Students()
            # s.students_name=gf.cleaned_data['students_name']
            # s.students_age=int(gf.cleaned_data['students_age'])
            # s.students_email=gf.cleaned_data['students_email']
            # s.students_password=gf.cleaned_data['students_password']
            gf.save()
            return HttpResponse("Data has been successfully saved...")
    else:
        gf=FillDetails()

    return render(request,'formapp/index.html',{'form':gf})

def Login(request):
    if request.method=='POST':
        pf=Log(request.POST)
        if pf.is_valid():
            email=pf.cleaned_data['email']
            password=pf.cleaned_data['password']
            # s=Students.objects.all()
            s=Students.objects.filter(students_email__exact=email,students_password__exact=password)
            return render(request,'formapp/details.html',{'params':s})

    else:
        pf=Log()
    return render(request,'formapp/login.html',{'log':pf})
