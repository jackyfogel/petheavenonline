from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('memorials/<slug:slug>', views.memorial, name='memorial'),
    
]