from django.shortcuts import render

# Create your views here.
def function(request):
    d={'a':'seshu'}
    return render(request,'h1.html',context=d)
def fun(request):
    d1={'x': 58}
    return render(request,'h2.html',d1)