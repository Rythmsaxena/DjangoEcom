from django.shortcuts import render
from django.http import HttpResponse
from shop.models import product

def index(request):
    products=product.objects.all()
    n=len(products)
    nslides=n//4+ceil(n/4-n//4)
    params={'products':products, 'no_of_slides':nslides , 'range':range(1,nslides)}

    return render(request, 'shop/indexshop.html',params)

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