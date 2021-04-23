from django.contrib import admin

from .models import Patient, Field, Schedule

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id','fname','lname','email','phone','date','checked')
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id','pid','timing','category','checked')


admin.site.register(Patient, PatientAdmin)
admin.site.register(Field)
admin.site.register(Schedule, ScheduleAdmin)