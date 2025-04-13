from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('blog/<int:year>/<int:month>/<slug:slug>/', views.post_detail, name='post_detail'),
]