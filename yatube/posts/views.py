from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import cache_page

from .forms import CommentForm, PostForm
from .models import Follow, Group, Post

User = get_user_model()


# @cache_page(20, key_prefix="index_page")
def index(request):
    posts = Post.objects.all()
    paginator = Paginator(
        posts,
        settings.NUMBER_POST
    )
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/index.html'
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    groups = group.posts.all()
    paginator = Paginator(
        groups,
        settings.NUMBER_POST
    )
    page_obj = paginator.get_page(
        request.GET.get('page')
    )
    template = 'posts/group_list.html'
    context = {'group': group, 'page_obj': page_obj}
    return render(request, template, context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    authors = author.posts.all()
    paginator = Paginator(
        authors,
        settings.NUMBER_POST
    )
    page_obj = paginator.get_page(
        request.GET.get('page')
    )
    following = None
    if request.user.is_authenticated:
        following = author.following.filter(user=request.user).exists()
    template = 'posts/profile.html'
    context = {
        'page_obj': page_obj,
        'author': author,
        'following': following
    }
    return render(request, template, context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    template = 'posts/post_detail.html'
    context = {
        'post': post,
        'requser': request.user,
        'comments': comments,
        'form': form,
    }
    return render(request, template, context)


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
    return redirect('posts:post_detail', post_id=post_id)


@login_required
def post_create(request):
    form = PostForm(
        request.POST or None,
        files=request.FILES or None)
    if form.is_valid():
        create_post = form.save(commit=False)
        create_post.author = request.user
        create_post.save()
        return redirect('posts:profile', create_post.author)
    template = 'posts/create_post.html'
    context = {'form': form}
    return render(request, template, context)


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return redirect('posts:post_detail', post_id)
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
        instance=post)
    if form.is_valid():
        form.save()
        return redirect('posts:post_detail', post_id)
    template = 'posts/create_post.html'
    context = {'form': form, 'post': post, 'is_edit': True}
    return render(request, template, context)


@login_required
def follow_index(request):
    posts = Post.objects.filter(
        author__following__user=request.user)
    paginator = Paginator(posts, settings.NUMBER_POST)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'posts/follow.html', context)


@login_required
def profile_follow(request, username):
    author = get_object_or_404(User, username=username)
    if author != request.user:
        Follow.objects.get_or_create(user=request.user, author=author)
    return redirect('posts:profile', author)


@login_required
def profile_unfollow(request, username):
    follow = get_object_or_404(
        Follow,
        user=request.user,
        author__username=username
    )
    follow.delete()
    return redirect('posts:profile', username)
