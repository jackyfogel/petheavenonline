from django.shortcuts import render, get_object_or_404
from .models import PetMemorial


# Create your views here.

def home(request):
    return render(request, 'petmemorial/index.html')

def memorial(request,slug):
    p = get_object_or_404(PetMemorial, slug=slug)
    return render(request, 'petmemorial/memorial.html', {'p': p})

