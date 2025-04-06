from django.shortcuts import render
from .models import BlogPost
from django.conf import settings
from django.http import HttpResponse

def blog_home(request):
    posts = BlogPost.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/blog_home.html', {'posts': posts})
# Create your views here.

def db_check(request):
    engine = settings.DATABASES['default']['ENGINE']
    name = settings.DATABASES['default']['NAME']
    return HttpResponse(f"🛠 DB Engine: {engine}<br>🗄 DB Name: {name}")
