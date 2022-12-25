from django.shortcuts import render

from datetime import datetime

from django.views.generic import ListView, DetailView

from .models import Post


class PostsList(ListView):
    model = Post
    ordering = '-created_at'
    context_object_name = 'posts'
    template_name = 'news/post_list.html'


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'news/post_details.html'
