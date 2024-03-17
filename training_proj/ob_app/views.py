from django.http import HttpResponse
from django.shortcuts import render
from .models import Blogs


def index(request):
    return HttpResponse("Welcome to OB")


def sample_template(request):
    users = [
        'Jeml',
        'Boja',
        'Abebe'
    ]

    # # Intialize the model object
    # blog = Blogs(title="New", page=33)
    # # Save the object into the database.
    # blog.save()

    # Fetch all
    blogs = Blogs.objects.all()
    print(blogs)

    # Get one
    blog = Blogs.objects.get(pk=1)
    print(blog)
    return render(request, 'welcome.html', context={'name': "Bantayehu", 'users': users})
