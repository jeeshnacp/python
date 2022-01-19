from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import message
from django.shortcuts import render
from .form import *
from . models import *
from django.shortcuts import render,redirect
# Create your views here.


def buyers(request):
    data=buyer.objects.all()
    return render(request,'buyer.html',{'data':data})

def sellers(request):
    data=seller.objects.all()
    return render(request,'seller.html',{'data':data})


def products(request):
    data=product.objects.all()

    return render(request,'product.html',{'data':data})



def dlt(request,id=None):
    data=product.objects.get(id=id)
    data.delete()
    return redirect('product')

def update(request,id=None):
    data=product.objects.get(id=id)
    if request.method=='POST':
        product_name=request.POST['product_name']
        price=request.POST['price']
        details=request.POST['details']
        data.product_name=product_name
        data.price=price
        data.details=details
        data.save()
        return redirect('product')
    return render(request,'update.html',{'data':data})

def formpro(request):
    if request.method=='POST':
        form=proform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form=proform()
        #form = proform(request.POST, request.FILES)
    return render(request,'update.html',{'form':form})

def selform(request):
    if request.method=='POST':
        form=sellerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seller')
    else:
        form=sellerform()
        #form = sellerform(request.POST)
    return render(request,'sellerform.html',{'form':form})

def buyform(request):
    if request.method=='POST':
        form=buyerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buyer')
    else:
        form=buyerform
        #form = buyerform(request.POST)
    return render(request,'buyerform.html',{'form':form})



def register(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'user creation successfull')
            return redirect('seller')
    return render(request,'register.html',{'form':form})


def custom_creation(request):
    form=customcreation()
    if request.method=='POST':
        form=customcreation(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'user creation successfull')
            return redirect('signup')
    return render(request,'signup.html',{'form':form})