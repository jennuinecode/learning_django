from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student
# Create your views here.
def index(request):
	return render(request, 'manager/index.html')

def success(request):
	return render(request, 'manager/index.html')

def registration(request):
	return render(request, 'manager/registration.html')

def register(request):
	if request.method == "POST":
		valid, response = Student.objects.validate_registration(request.POST)
		if valid:
			messages.success(request, "Congrats, {}! You've successfully registered! Now Log In!".format(response.first_name))
			request.session['user_id'] = response.id
			return redirect('manager:success')
		else:
			for error in response:
				messages.error(request, error)

	return redirect('manager:index')

def login(request):
	if request.method == "POST":

		valid, response = Student.objects.login_check(request.POST)
		if valid:
			static_path = "../static/manager/images/{}.jpg" .format(response.house)

			request.session['first_name'] = response.first_name
			request.session['house'] = response.house
			request.session['user_id'] = response.id

			context = {
				'first_name': response.first_name,
				'house': response.house,
				'static_path': static_path,
			}
			#assigning each house to a bootstrap color so that buttons match house colors
			print request.session['house']

			return render(request, 'courses/index.html', context)
		else:
			for error in response:
				messages.error(request, error)

	return redirect('manager:index')


def logout(request):
    if request.method == "POST":
        if 'user_id' in request.session:
            del request.session['user_id']
            print "user has logged out!"
    return redirect('manager:index')
