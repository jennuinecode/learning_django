from django.shortcuts import render, redirect
import re
from .models import User

def index(request):

    context = {
        'users': User.objects.all(),
    }

    return render(request, 'registration/index.html', context)

def register(request):
    print "made it to register method ****************"

    if not re.match( r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", request.POST['email']):
            context = {
                'messages': []
            }
            if messages not in context:
                print "please enter valid email **************"
                context['messages'].append("please enter valid email address")

    else:
        User.objects.create(email=request.POST['email'])
        print "email successfully added **************"
    return redirect('/')
