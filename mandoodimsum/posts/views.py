from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm

def index(request):
    posts = Post.objects.all().order_by('-pk')
    return render(request, 'posts/index.html', {'posts': posts})


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form': form})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment_set.all()
    form = CommentForm()
    return render(request, 'posts/detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })


@login_required
def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user != request.user:
        return redirect('posts:index')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/update.html', {'form': form})


@login_required
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user == request.user:
        post.delete()
    return redirect('posts:index')


@login_required
def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
    return redirect('posts:detail', pk)


@login_required
def comment_delete(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
    return redirect('posts:detail', pk)