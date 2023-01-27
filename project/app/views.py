from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post
from .filters import PostFilter
from .forms import PostForm


class PostsList(ListView):
    model = Post
    ordering = '-created_at'
    context_object_name = 'posts'
    template_name = 'news/post_list.html'
    queryset = Post.objects.all()
    paginate_by = 3


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'news/post_details.html'


class PostSearch(ListView):
    model = Post
    ordering = '-created_at'
    template_name = 'news/post_search.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('app.add_post',)
    template_name = 'news/post_create.html'
    form_class = PostForm
    success_url = '/news/'
    raise_exception = True


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('app.change_post',)
    template_name = 'news/post_update.html'
    form_class = PostForm
    success_url = '/news/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('app.delete_post',)
    template_name = 'news/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
