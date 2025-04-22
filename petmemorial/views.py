from django.shortcuts import render, get_object_or_404, redirect
from .models import PetMemorial
from .forms import EmailRegistrationForm
from django.core.mail import send_mail
from django.contrib import messages
import os

def home(request):
    return render(request, 'petmemorial/index.html')

def memorial(request, slug):
    p = get_object_or_404(PetMemorial, slug=slug)
    return render(request, 'petmemorial/memorial.html', {'p': p})

def register_view(request):
    if request.method == 'POST':
        form = EmailRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            send_mail(
                subject='Welcome to Pet Heaven 🐾',
                message='Thanks for signing up! You can now create memorials for your beloved pets.',
                from_email=os.getenv('EMAIL_HOST_USER'),
                recipient_list=[user.email],
            )
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
    else:
        form = EmailRegistrationForm()

    return render(request, 'petmemorial/register.html', {'form': form})
