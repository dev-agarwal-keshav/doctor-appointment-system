from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from consult.models import Patient, Field, Schedule
from .models import Doctor, Record
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    if request.method=='POST':
        mail = request.POST.get('email', '')
        user_password = request.POST.get('password', '')
        user = authenticate(username=mail, password=user_password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in")
            return redirect('/doctor/pat')
        else:
            messages.error(request, "No user exists with that credentials")
            return redirect('/')
    return render(request,'doctor/login.html')


def patients(request):
    print(request.user.username)
    doc = Doctor.objects.get(email=request.user.username)
    ik = Field.objects.get(category=doc.category)

    sch = Schedule.objects.filter(category=doc.category, checked=False)
    # print(patient)
    return render(request, 'doctor/index.html', {'sch': sch})

def checkup(request, id):
    pat=Patient.objects.get(id=id)
    rec=Record.objects.filter(patient=pat)

    record=False
    if rec :
        record=True
    return render(request, 'doctor/checkup.html',{'pat':pat, 'record': record})

def save(request,id):
    doc = Doctor.objects.get(email="k@gmail.com")
    pat = Schedule.objects.get(pid=id, category=doc.category)
    pat1 = Patient.objects.get(id=id)
    ail=request.POST.get('ail','')
    susp=request.POST.get('susp','')
    med=request.POST.get('med','')
    record=Record(patient=pat1, ail=ail,med=med, susp=susp, doctor=doc)
    record.save()
    pat.checked=True
    pat1.checked=True
    pat.save()
    pat1.save()
    return redirect('/doctor/pat')

def prev_rec(request, id):
    pat=Patient.objects.get(id=id)
    rec=Record.objects.filter(patient=pat).order_by('date')
    return render(request, 'doctor/prev_record.html',{'rec':rec})