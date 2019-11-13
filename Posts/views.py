from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from .forms import PostForm
from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'all_the_posts'
    template_name = 'post-list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'that_one_post'
    template_name = 'post-detail.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post-create.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
