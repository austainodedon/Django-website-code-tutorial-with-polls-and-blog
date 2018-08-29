from django.shortcuts import render

def index(request):
    return render(request, 'home/home.html')

def contact(request):
    return render(request, 'home/basic.html', {'content':['If you would like to contact me, call +2347067162698 or please email me','tclassified.com@gmail.com']})
