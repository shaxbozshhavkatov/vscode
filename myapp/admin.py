from django.contrib import admin
from .models import *
# Register your models here.


class New(admin.ModelAdmin):
    list_display = ['name']
    
admin.site.register(PhoneModel,New)

class New1(admin.ModelAdmin):
    list_display = ['color','storage','region','name1']
    
admin.site.register(InfoModell,New1)