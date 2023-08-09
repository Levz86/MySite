from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

urlpatterns = [
    #path('', views.index),
    path('Jelly_Jumpers', views.Jelly_Jumpers),
    path('about', views.about),
    path('contact', views.contact),

    path('',
        ListView.as_view(
            queryset=
            Post.objects.all().order_by("-date")[:25],
            template_name="blog.html"
            )
        ),
    path('<int:pk>/',
        DetailView.as_view(
            model = Post,
            template_name="post.html"
            ),
            name = "artical-detail"
        ),
    path('add_post/', 
        views.createview.as_view(),
          name = "add_post")
]