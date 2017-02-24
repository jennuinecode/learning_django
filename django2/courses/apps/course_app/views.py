from django.shortcuts import render, redirect
from . models import Course

def index(request):

    context= {
        'courses': Course.objects.all()
    }

    return render(request, 'course_app/index.html', context)

def add(request):

    new_course = Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    new_course.save()
    print new_course
    return redirect('/')

# def destroy(request):
#
#     return render(request, 'course_app/destroy.html')
