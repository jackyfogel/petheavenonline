from django.db import models
from .storage_backends import MediaStorage
# Create your models here.

class BlogPost(models.Model):
    title= models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    seo_title = models.CharField(max_length=70, null=True, blank=True)
    seo_description = models.CharField(max_length=200, null=True, blank=True)
    canonical_url = models.URLField(blank=True, null=True)
    noindex = models.BooleanField(default=False)
