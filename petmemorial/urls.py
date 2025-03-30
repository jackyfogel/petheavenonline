from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('memorial', views.memorial, name='memorial')
]