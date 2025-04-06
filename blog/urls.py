from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('db-check/', views.db_check, name='db_check'),
]