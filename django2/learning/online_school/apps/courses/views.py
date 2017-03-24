from django.shortcuts import render, redirect
from . models import Course
from ..manager.models import Student

def index(request):
    context= {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)


def add(request):
    # creates new class or stuents to register to


    Course.objects.create(name=request.POST['name'],  description=request.POST['description'])

    return redirect('manager:home')

def join(request, id):


    user_id = request.session['user_id']

    my_course = Course.objects.get(id=id)
    student = Student.objects.get(id=user_id)
    my_course.students.add(student)
    my_course.save()





    return redirect('manager:home')


def edit(request, id):

    pass

def drop(request, id):
    pass

    user_id = request.session['user_id']

    my_course = Course.objects.get(id=id)
    student = Student.objects.get(id=user_id)
    my_course.students.remove(student)


    return redirect('manager:home')



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
