from django.shortcuts import render
from .models import *

# Create your views here.

def HomePage(request):
    context = InfoModell.objects.all()
    return render(request,'blog.html',{'context':context})
    return

def aboutpage(request,name):
    obj = InfoModell.objects.get(name = name)
    Name = PhoneModel.objects.all()
    return render(request,'detail.html',{'obj':obj,"Name":Name})

