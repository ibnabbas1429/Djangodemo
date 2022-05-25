
from django.shortcuts import render

from django.urls import path

# Create your views here.
from . models import Students

def home(request):

    student = Students.objects.all()
    context = {'student' : student}
    return render(request , 'home.html' , context)
