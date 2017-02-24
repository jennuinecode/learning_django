from django.shortcuts import render

def index(request):
    context = {
        "email" : "hpotter@hogwarts.com",
        "name" : "Harry"
    }
    return render(request, "first_app/index.html", context)


def show(request, id):
    context = {
        "id" : id,
    }
    return render(request, "first_app/show.html", context)
