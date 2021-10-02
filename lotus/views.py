from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample1(request):
    return render(request,'index.html')

def sample2(request,name):
    context={'a': name

    }
    return render(request,'sample.html',context=context)

def sample3(request):
    return HttpResponse("hello3")

def argument(request,name):
    return HttpResponse("hello"+ name)