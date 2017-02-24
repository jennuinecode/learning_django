from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'store_front/index.html')

def women(request):
    return render(request, 'store_front/womenproducts.html')

def men(request):
    return render(request, 'store_front/menproducts.html')
