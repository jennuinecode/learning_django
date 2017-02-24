from django.shortcuts import render

def index(request):
    return render(request, 'baked_potato/index.html')

def shop(request):
    return render(request, 'baked_potato/shop.html')
