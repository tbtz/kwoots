from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from .forms import PostForm
from .models import Post
from django.shortcuts import redirect, render


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post-list.html'


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'post-list.html', context)


class PostDetailsView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post-details.html'


def post_details(request, **kwargs):
    post_id = kwargs['pk']
    if request.method == 'POST':
        Post.objects.filter(id=post_id).delete()
        return redirect('post_list')
    else:
        post = Post.objects.get(id=post_id)
        context = {'post': post}
        return render(request, 'post-details.html', context)


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create-post.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            print(form)
            form.save()
            return redirect('post_list')
        else:
            print(form.errors)
            return render(request, 'create-post.html', {'form': form})

    else:
        form = PostForm()
        context = {'form': form}
        return render(request, 'create-post.html', context)
