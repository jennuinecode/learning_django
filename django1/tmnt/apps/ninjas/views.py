from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'ninjaapp/index.html')

def show(request, ninja_color):

    if ninja_color == 'red':
        context= {
            'image':'ninjaapp/raphael.jpg'
        }
    elif ninja_color == 'blue':
        context= {
            'image':'ninjaapp/leonardo.jpg'
        }
    elif ninja_color == 'purple':
        context= {
            'image':'ninjaapp/donatello.jpg'
        }
    elif ninja_color == 'orange':
        context= {
            'image':'ninjaapp/michaelangelo.jpg'
        }
    else:
        context= {
            'image':'ninjaapp/april.jpg'
        }
    """
    return render(request,'ninjaapp/index.html',context)
