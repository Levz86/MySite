from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

''' This is the second docstring'''

# Create your views here.

def Jelly_Jumpers(request):
    return render(request, "Jelly_Jumpers.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

class homeview(ListView):
    model = Post
    template_name = 'blog.html'

class detailview(DetailView):
    model = Post
    template_name = 'post.html'

class createview(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'

