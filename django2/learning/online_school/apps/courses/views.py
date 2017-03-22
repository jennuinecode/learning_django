from django.shortcuts import render, redirect
from . models import Course

def index(request):
    context= {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)


def add(request):
    print "made it to add function ********************************"

    Course.objects.create(name=request.POST['name'],  description=request.POST['description'])

    print "added!!!!! ********************************"

    return redirect('manager:success')


# def remove(request, id):
#     context= {
#         'courses': Course.objects.filter(id=id)
#     }
#     course = Course.objects.get(id=id)
#
#     return render(request, 'courses/remove.html', context)


def confirm(request, id):
    context= {
        'courses': Course.objects.filter(id=id)
    }
    course = Course.objects.get(id=id)

    Course.objects.filter(id=id).delete()

    return render(request, 'courses/index.html')
