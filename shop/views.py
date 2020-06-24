from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'shop/indexshop.html')

def about(request):
    return HttpResponse('about page')

def contact(request):
    return HttpResponse('contact')

def tracker(request):
    return HttpResponse('tracker page')

def about(request):
    return HttpResponse('about page')

def productview(request):
    return HttpResponse('product view page')

def checkout(request):
    return HttpResponse('checkout page')

def search(request):
    return HttpResponse('search page')