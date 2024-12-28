from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post, Comment, Reply
from .forms import PostForm, CommentForm, ReplyForm

def home(request):
    return render(request, 'index.html')
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'main/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid() and request.user.is_authenticated:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        comment_form = CommentForm()
    
    return render(request, 'main/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'main/post_form.html', {'form': form})

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({'likes_count': post.total_likes(), 'liked': liked})

@login_required
def add_reply(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.comment = comment
            reply.author = request.user
            reply.save()
            return redirect('post_detail', pk=comment.post.pk)
    return redirect('post_detail', pk=comment.post.pk)