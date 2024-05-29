from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
class Home(ListView):
    model = Post
    template_name = 'posts/home.html'

class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/add.html'
    success_url = reverse_lazy("posts:home")
