from django.db import models

# Create your models here.
class Field(models.Model):
    category=models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Patient(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField(default=0)
    checked=models.BooleanField(default=False)
    date=models.DateField(auto_now_add=True)
    category=models.ManyToManyField(Field)
    age=models.IntegerField(default=11)


class Schedule(models.Model):
    pid=models.ForeignKey(Patient,on_delete = models.CASCADE)
    timing=models.CharField(max_length=100,default='')
    category=models.CharField(max_length=100,default='')
    checked = models.BooleanField(default=False)







