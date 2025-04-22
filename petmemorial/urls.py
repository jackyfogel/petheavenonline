from django.urls import path
from . import views  # import the whole views module

urlpatterns = [
    path('', views.home, name='home'),
    path('memorials/<slug:slug>/', views.memorial, name='memorial'),
    path('register/', views.register_view, name='register'),
]
