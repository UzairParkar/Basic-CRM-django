from django.contrib import admin
from .models import Record

# Register your models here.
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','phone','city','state']
    list_filter = ('id',)
