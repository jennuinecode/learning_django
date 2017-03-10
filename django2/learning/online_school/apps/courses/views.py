from django.shortcuts import render, redirect
from . models import Course

def index(request):
    context= {
        'courses': Course.objects.all()
    }
    return render(request, 'courses:index', context)


def add(request):
    print "made it to add function ********************************"

    Course.objects.create(name=request.POST['name'], description=request.POST['description'])

    return redirect('courses:index')


def remove(request, id):
    context= {
        'courses': Course.objects.filter(id=id)
    }
    course = Course.objects.get(id=id)

    return render(request, 'courses:remove', context)


def confirm(request, id):
    context= {
        'courses': Course.objects.filter(id=id)
    }
    course = Course.objects.get(id=id)

    Course.objects.filter(id=id).delete()

    return render(request, 'courses:index')
