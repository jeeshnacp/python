from django.shortcuts import render

# Create your views here.
def std(request):
    return render(request,'studentbook.html')