from django.shortcuts import render, HttpResponse
from .models import User

def index(request):

    return HttpResponse(User.UserManager.login("hpotter@gryffindor.com", "hedwig"))
