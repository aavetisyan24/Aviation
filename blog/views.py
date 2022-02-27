from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# posts = [
#     {
#         "author": "Artak Avetisyan",
#         "title": "Blog Post1",
#         "content": "First Post",
#         "date_posted": "30 November 2021"
#     },
#     {
#         "author": "Hasmik Amiryan",
#         "title": "Blog Post2",
#         "content": "Second Post",
#         "date_posted": "29 November 2021"
#     }
# ]


def home(request):
    context = {
       "posts": Post.objects.all()
    }
    return render(request, "blog/home.html", context)

# def airlines(request):
#     return HttpResponse("Hello Airlines")


def about(request):
    return render(request, "blog/about.html", {"title": "About"})


def flyto(request):
    return render(request, "blog/flyto.html", {"title": "Fly To"})


def airlines(request):
    return render(request, "airlines/search.html", {"title": "Search"})

