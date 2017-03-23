from django.shortcuts import render, redirect
from . models import Course

def index(request):
    context= {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)


def add(request):
    print "made it to add function ********************************"


    static_path = "../static/manager/images/{}.jpg".format(response.house)
    Course.objects.create(name=request.POST['name'],  description=request.POST['description'])

    context = {
        'courses': Course.objects.all(),
        'static_path': static_path

    }
    print "added!!!!! ********************************"

    return render(request, 'manager/home.html', context)


def remove(request, id):
    context= {
        'courses': Course.objects.filter(id=id)
    }
    course = Course.objects.get(id=id)

    return render(request, 'courses/remove.html', context)


def confirm(request, id):
    context= {
        'courses': Course.objects.filter(id=id)
    }
    course = Course.objects.get(id=id)

    Course.objects.filter(id=id).delete()

    return render(request, 'courses/index.html')
