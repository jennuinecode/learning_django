from django.shortcuts import render
from .models import Student
import re

def index(request):

    return render(request, 'login/index.html')


def register(request):

    return render(request, 'login/register.html')

def add(request):

    error = False
    # static_path = "../static/login/images/{}.jpg".format(request.POST['house'])
    context = {
        'message': "Successfully Registered. Now you an login"
    }

    if request.method == 'POST':
        if not re.match( r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", request.POST['email']):
            context['email'] = "Please enter a valid email"
            error = True
        if len(request.POST['first_name']) < 2:
            context['first_name'] = "Name must be longer than 2 characters"
            error = True
        if len(request.POST['last_name']) < 2:
            context['last_name'] = "Name must be longer than 2 characters"
            error = True
        if len(request.POST['password']) < 7:
            context['password'] = "Name must be longer than 2 characters"
            error = True
    if error == False:
        Student.objects.create(house=request.POST['house'], first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])

    return render(request, 'login/index.html', context)


def logout(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")
