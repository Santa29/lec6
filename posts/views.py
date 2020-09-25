from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView

from .models import Post 

from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(LoginRequiredMixin,ListView):
    model = Post 
    template_name = 'post_list.html'
    context_object_name = 'post_list'
    login_url = 'login'

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ('title', 'body')
    login_url = 'login'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('post_list')
    login_url = 'login'

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    login_url = 'login'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ('title', 'body')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)