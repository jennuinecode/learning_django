from django.shortcuts import render, redirect
from . models import Course

def index(request):
    context= {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)


def add(request):
    # creates new class or stuents to register to


    Course.objects.create(name=request.POST['name'],  description=request.POST['description'])

    return redirect('manager:home')

def join(request):

    pass

def edit(request):

    pass

def remove(request, id):
    context= {
        'courses': Course.objects.filter(id=id)
    }
    course = Course.objects.get(id=id)

    return render(request, 'courses/remove.html', context)


def confirm(request, id):


    course = Course.objects.get(id=id)

    course.delete()

    return redirect('manager:home')
