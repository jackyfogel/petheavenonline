from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('<int:year>/<int:month>/<slug:slug>/', views.blog_post, name='blog_post'),
]