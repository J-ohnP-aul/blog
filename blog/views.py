from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Post

# Create your views here.

def post_list(request):
  post = Post.published.all()
  return render(request, 'blog/post/list.html', {'post':post})

def post_detail(request, year, month, day, post):
  # try:
  #   post = Post.published.get(id=id)
  # except Post.DoesNotExist:
  #   raise Http404("No Post Foundn !!")
  post = get_object_or_404(
    Post,
    id=id,
    status = Post.Status.PUBLISHED,
    slug = post,
    publish__year=year,
    publish__month=month,
    publish__day = day
  )
  return render(request, 'blog/post/detail.html', {'post':post})
