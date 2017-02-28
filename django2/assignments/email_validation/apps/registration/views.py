from django.shortcuts import render, redirect
import re
from .models import User



def index(request):

    return render(request, 'registration/index.html')

def register(request):

    errors = {
        'users':User.objects.all(),
    }
    print "made it to register method ****************"

    if not re.match( r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", request.POST['email']):
        print "please enter valid email **************"
        errors['invalidEmail'] = "Please enter a valid email"
    else:
        User.objects.create(email=request.POST['email'])
        print "email successfully added **************"
        errors['success'] = "Successfully registered"


    return render(request, 'registration/index.html', errors)
