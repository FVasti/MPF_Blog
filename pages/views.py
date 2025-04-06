from django.shortcuts import render

from .models import Post
from .forms import PostForm

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin

from django.views.generic.edit import DeleteView



class AboutView(TemplateView):
    template_name = "about.html"

class PostListView(ListView):
    model = Post
    template_name = 'pages/post_list.html'
    context_object_name = 'posts'
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'subtitle', 'content', 'image']
    template_name = 'pages/post_form.html'
    success_url = reverse_lazy('posts_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'subtitle', 'content', 'image']
    template_name = 'pages/post_form.html'
    success_url = reverse_lazy('posts_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'pages/post_confirm_delete.html'
    success_url = reverse_lazy('posts_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'pages/post_list.html', {'posts': posts})