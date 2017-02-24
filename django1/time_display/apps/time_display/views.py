from django.shortcuts import render
import datetime


def index(request):
    currentDateTime = datetime.datetime.now()
    context={
    "currentDateTime":currentDateTime
    }
    return render(request, 'time_display/index.html', context)
