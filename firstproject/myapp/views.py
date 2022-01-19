from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def my(request):
    return HttpResponse("hello world")



def  image(request):
    return render(request,'index.html')