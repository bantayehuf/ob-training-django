from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Blogs
from .forms import BlogForm


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
    # return render(request, 'welcome.html', context={'name': "Bantayehu", 'users': users})

    return redirect('ob.index')


def blog_mgt(request):
    message = ''
    if request.method == 'POST':
        data = BlogForm(request.POST)

        if data.is_valid():
            message = 'Form sumited successfully'
            print('Submited title is:- ', data.cleaned_data['title'])

    form = BlogForm()

    return render(request, 'blog.html', {'form': form, 'message': message})
