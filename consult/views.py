from django.shortcuts import render, HttpResponse, redirect
from .models import Patient, Field, Schedule
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from doctor.models import Doctor, Record
from fpdf import FPDF
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

# Create your views here.

def index(request):
    field=Field.objects.all()
    doc=Doctor.objects.all()
    return render(request,'consult/index.html', {'field':field, 'doc':doc})

def submit(request):
    if request.method=='POST':
        fname=request.POST.get('fname','')
        lname=request.POST.get('lname','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        appointfor=request.POST.get('appointfor','')
        already=request.POST.get('already','')
        doctor=request.POST.get('doctor','')
        if not Doctor.objects.filter(name=doctor, category=appointfor):
            messages.error(request, doctor+" is not "+appointfor)
            return redirect('/')
        #print(doctor)
        field=Field.objects.all()
        fields={}
        for i  in field:
            fields[i.category]=i.id
        if already=='yes':
            patientID = request.POST.get('patientID', '')
            p=Patient.objects.get(id=patientID)

            if p.email==email:
                pat=Patient.objects.get(id=patientID)
                pat.category.add(fields[appointfor])
                k = timeslot(patientID, appointfor)
                sch=Schedule(pid=pat, timing=k, category=appointfor, checked=False)
                sch.save()


        else:
            pat=Patient(fname=fname,lname=lname,email=email,phone=phone,checked=False)
            pat.save()
            pat.category.add(fields[appointfor])
            patientID=pat.id
            k = timeslot(patientID, appointfor)
            sch = Schedule(pid=pat, timing=k,category=appointfor, checked=False)
            sch.save()

    return redirect('/')

def timeslot(patientID, appointfor):
    patient=Schedule.objects.filter(category=appointfor)
    j=len(patient)
    slot=['10-11','11-12','12-13','13-14','14-15','15-16','16-17','17-18']
    timel=int(j/2)
    return slot[timel]


def about(request):
    return render(request,'consult/about.html')

def records(request):
        if request.method=='POST':
            patid= request.POST.get('patID', '')
            email = request.POST.get('email', '')
            cat=request.POST.get('category','')
            pat=Patient.objects.get(id=patid,email=email)
            doc=Doctor.objects.get(category=cat)
            record=Record.objects.filter(patient=pat,doctor=doc)
            i=record[len(record)-1]
            email_sub= 'Your latest records for Dr.'+doc.name
            message = render_to_string('record/send_record.html',
                                       {
                                           'pat':pat,
                                           'doctor':doc,
                                           'record':i,
                                       })
            email = EmailMessage(
                email_sub,
                message,
                settings.EMAIL_HOST_USER,
                [email]
            )

            email.send()
            messages.success(request, "Your records has been shared to you via email at the email address you provided")
            return redirect('/schedule')
        field = Field.objects.all()
        return render(request,'consult/records.html',{ 'field':field})

def schedule(request):
    if request.method=='POST':
        patid= request.POST.get('patID', '')
        email = request.POST.get('email', '')
        try:
            pat=Patient.objects.get(id=patid,email=email, checked=False)
            if pat is not None:
                sch=Schedule.objects.filter(pid=patid)
                doc = Doctor.objects.all()
                return render(request, 'consult/schedule.html', {'sch': sch, 'doc':doc})
        except:
            messages.error(request, "Sorry you dont have any appointment with this ID")
            return redirect('/schedule')

    return render(request,'consult/schedule.html')

