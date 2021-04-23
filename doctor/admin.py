from django.contrib import admin
from .models import Doctor, Record
# Register your models here.
class DocAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone','lic','age','category')

class RecordAdmin(admin.ModelAdmin):
    list_display = ('id','patient','doctor','ail','med','susp','date')

admin.site.register(Doctor,DocAdmin)
admin.site.register(Record,RecordAdmin)