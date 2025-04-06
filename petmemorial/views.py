from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'petmemorial/index.html')

def memorial(request):
    return render(request, 'petmemorial/memorial.html')