from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from blog.forms import PostForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/main.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'

class PostCreateView(PermissionRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    permission_required = 'blog.create_post'
    template_name = 'blog/add_post.html'
    success_url = reverse_lazy('blog:main')

class PostUpdateView(PermissionRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    permission_required = 'blog.update_post'
    template_name = 'blog/edit_post.html'
    success_url = reverse_lazy('blog:main')

@permission_required('blog.delete_post')
def post_delete(request, pk):
    client_to_delete = Post.objects.get(pk=pk)
    client_to_delete.delete()
    return HttpResponseRedirect(reverse_lazy('blog:main'))