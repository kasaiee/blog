from django.shortcuts import render
from django.http import Http404
from blog.models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, id):
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No Post found.")
    post = get_object_or_404(Post, id=id, status='PB')
    return render(request, 'blog/post/detail.html', {'post': post})