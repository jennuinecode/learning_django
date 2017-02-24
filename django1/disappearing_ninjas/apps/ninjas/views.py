from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'ninjas/index.html')


def ninja(request, color):
	colors = {
		'purple': "donatello",
		'blue': "leonardo",
		'orange': "michelangelo",
		'red': "raphael",

	}



	try:
		print colors[color]
		print color
		static_path = "../static/ninjas/images/{}.jpg".format(colors[color])

	except:
		static_path = "../static/ninjas/images/{}.jpg".format("april")

	context = {
		'static_path': static_path
	}

	return render(request, 'ninjas/show.html', context)
