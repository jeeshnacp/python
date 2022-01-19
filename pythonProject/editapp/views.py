
from django.shortcuts import render,redirect
from . models import *
from .forms import *

# Create your views here.
def my(request):
    return render(request,'index.html')

def student(request):
    data =stud.objects.all()
    return render(request,'studentindex.html',{'data1':data})



def dlt(request,id=None):
    data = stud.objects.get(id=id)
    data.delete()
    return redirect('home')

def createstd(request):
    if request.method == "POST":
        # stud_id = request.POST["stud_id"]
        # stud_name = request.POST["stud_name"]
        # age = request.POST["age"]
        # stud.objects.create(stud_id=stud_id,stud_name=stud_name,age=age)
        form = stdform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=stdform()
    return render(request,'createstd.html',{'form':form})

def updatestd(request,id=None):
    data = stud.objects.get(id=id)
    if request.method == "POST":
        stud_id = request.POST["stud_id"]
        stud_name = request.POST["stud_name"]
        age = request.POST["age"]
        #stud.objects.create(stud_id=stud_id,stud_name=stud_name,age=age)

        data.stud_id = stud_id
        data.stud_name = stud_name
        data.age = age
        data.save()
        return redirect('home')
    return render(request,'createstd.html',{'data':data})

def viewstd(request):
    data=students.objects.all()
    return render(request,'viewclass.html',{'data':data})

def viewcls(request):
     data=classs.objects.all()
     return redirect('home')
     return render(request,'viewclass.html',{'data':data})
