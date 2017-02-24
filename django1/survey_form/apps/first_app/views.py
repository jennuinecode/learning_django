from django.shortcuts import render, redirect

def index(request):
    return render(request, 'first_app/index.html')

def create(request):
    if request.method == "POST":
        request.session['name'] = request.POST['first_name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']

        return render(request, 'first_app/result.html')

    else:
        return redirect('/')

#
def goback(request):
    if request.method == "POST":
        return redirect('/')
