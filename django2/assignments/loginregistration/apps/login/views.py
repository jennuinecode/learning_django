from django.shortcuts import render, redirect
from .models import Student
import re

def index(request):

    return render(request, 'login/index.html')


def register(request):

    return render(request, 'login/register.html')

def create(request):


    # static_path = "../static/login/images/{}.jpg".format(request.POST['house'])

    if request.method == 'POST':
        response = Student.objects.validateRegistration(request.POST)
        if response[0] == False:
            for err in response[1]:
                messages.error(request,err)
            return redirect('/register')
        else:
            # here i will add students id and house to session
            return redirect('/commonroom')
    else:
        return redirect('/register')

def commonroom(request):

    # Student.objects.filter(id=request.session['id'])

    return render(request, 'login/commonroom.html')
