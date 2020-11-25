from django.shortcuts import render
from django.http import HttpResponse
from .models import Prebuilt_70k,Prebuilt_80k,Prebuilt_90k,Prebuilt_1L
from fetch_price import *
import re
# Create your views here.
def home(request):
    return render(request,'home/index.html')

def about(request):
    
    return render(request,'home/about.html')

def contact(request):
    
    return render(request,'home/contact.html')

def desktop(request):

    data70k=Prebuilt_70k.objects.all()
    data80k=Prebuilt_80k.objects.all()
    data90k=Prebuilt_90k.objects.all()
    data1l=Prebuilt_1L.objects.all()


    return render(request,'home/desktop.html',{'data70k':data70k,'data80k':data80k,'data90k':data90k,'data1l':data1l})

def update(request):
    price=[]
    for i in range (2,10):
        price.append(fetch_prices(2,i))
    i=0
    data70k=Prebuilt_70k.objects.all()
    data80k=Prebuilt_80k.objects.all()
    data90k=Prebuilt_90k.objects.all()
    data1l=Prebuilt_1L.objects.all()
    for item in data70k:
        item.price=price[i]
        i+=1
        item.save()
    return render(request,'home/update.html')





