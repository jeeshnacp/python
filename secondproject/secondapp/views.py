from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def fun(request):
    return HttpResponse("hiiiii")