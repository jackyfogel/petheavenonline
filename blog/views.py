from django.shortcuts import render
from .models import BlogPost

def blog_home(request):
    posts = BlogPost.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/blog_home.html', {'posts': posts})
# Create your views here.
