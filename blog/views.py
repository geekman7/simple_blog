from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView 
from django.views import generic
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request,'blog/index.html')

class CreatePost(CreateView):
    model = Post
    fields = ['title', 'content']

class PostList(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date']

class DetailPost(LoginRequiredMixin,generic.DetailView):
    model = Post
    

class UpdatePoste(generic.UpdateView):
    model = Post
    fields = ['title', 'content']


class DeletePost(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blog:blog-index')
