from django.shortcuts import render
from .models import User

def index(request):

    People.objects.create(first_name="Harry", last_name="Potter")
    people = People.objects.all()
    print people
    context = {
        'people': people
    }
    return render(request, 'firstapp/index.html', context)
