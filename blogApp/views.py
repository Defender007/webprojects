from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blogApp/post/list.html',
                  {'posts': posts})
    # return HttpResponse('It worked')


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year, publish__month=month,
                             publish__day=day)
    return render(request,
                  'blogApp/post/detail.html',
                  {'post': post})
