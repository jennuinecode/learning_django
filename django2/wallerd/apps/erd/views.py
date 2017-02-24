from django.shortcuts import render, redirect
from . models import Blog, Comment

def index(request):
    context = {
        'blogs': Blog.objects.all()
        # select * from Blog
    }
    return render(request, 'erd/index.html', context)

def blogs(request):
    #using ORM
    Blog.objects.create(title=request.POST['title'], blog=request.POST['blog'])
    #insert ing blogs (title, blog) values (title, blog) + created/updated at
    return redirect('/')

def comments(request, id):
    blog = Blog.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'], blog_id=blog )

    return redirect('/')
