from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'petmemorial/index.html')

def memorial(request):
    return render(request, 'petmemorial/memorial.html')