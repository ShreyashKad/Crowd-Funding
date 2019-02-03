from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

def view_home(request):#for investor login html page
    return render(request,'home/index.html')
