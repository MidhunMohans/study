from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Subject, lead


def demo(request):
    obj=Subject.objects.all()
    ob=lead.objects.all()

    return render(request,"index.html",{'result':obj,'result1':ob})
# def addition(request):
#     x=float(request.GET['num1'])
#     y=float(request.GET['num2'])
#     res=x+y
#     res1=x-y
#     res2=x*y
#     res3=x/y
#     return render(request,'about.html',{'result':res,'result1':res1,'result2':res2,'result3':res3})