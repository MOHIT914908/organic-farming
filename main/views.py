from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def achivement(request):
    return render(request, 'achivement.html')

def fairs(request):
    return render(request, 'fairs.html')

def shops(request):
    return render(request, 'shops.html')

def contact(request):
    return render(request, 'contactus.html')

def about(request):
    return render(request,'about.html')
