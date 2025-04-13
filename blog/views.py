from django.shortcuts import render, get_object_or_404
from .models import BlogPost
# Create your views here.

def blog_home(request):
    return render(request,'blog/index.html')

def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
