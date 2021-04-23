from django.db import models

from consult.models import Patient
# Create your models here.

class Doctor(models.Model):
    name=models.CharField(max_length=100,default="")
    age=models.IntegerField(default=0)
    email=models.EmailField()
    category=models.CharField(max_length=100)
    lic=models.CharField(max_length=100)
    phone=models.IntegerField()

class Record(models.Model):
    patient=models.ForeignKey(Patient,on_delete = models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete = models.CASCADE, default="")
    date=models.DateField(auto_now_add=True)
    ail=models.TextField()
    susp=models.TextField()
    med=models.TextField()
