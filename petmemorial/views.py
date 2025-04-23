from django.shortcuts import render, get_object_or_404, redirect
from .models import PetMemorial
from .forms import EmailRegistrationForm
from django.core.mail import send_mail
from django.contrib import messages
import os
from django.contrib.auth.decorators import login_required
from .forms import PetMemorialForm

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

            try:
                send_mail(
                    subject='Welcome to Pet Heaven 🐾',
                    message='Thanks for signing up! You can now create memorials for your beloved pets.',
                    from_email=os.getenv('EMAIL_HOST_USER'),
                    recipient_list=[user.email],
                    fail_silently=False,
                )
            except Exception as e:
                messages.error(request, f'Something went wrong sending email: {e}')

            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            print("💥 FORM ERRORS:", form.errors)  # 👈 LOG FORM ERRORS TO TERMINAL
            messages.error(request, 'Something went wrong with your form. Please try again.')

    else:
        form = EmailRegistrationForm()

    return render(request, 'petmemorial/register.html', {'form': form})

@login_required
def create_memorial(request):
    if request.method == 'POST':
        form = PetMemorialForm(request.POST, request.FILES)
        if form.is_valid():
            memorial = form.save(commit=False)
            memorial.user = request.user
            memorial.status = 'pending'
            memorial.save()
            print("📬 Sending to:", request.user.email)
            send_mail(
                subject='Memorial Submitted – Pending Approval 🐾',
                message=f'Thank you {request.user.username}, your memorial for {memorial.pet_name} is awaiting approval.',
                from_email=os.getenv('EMAIL_HOST_USER'),
                recipient_list=[request.user.email],
                fail_silently=False,
            )

            messages.success(request, 'Your memorial has been submitted and is pending approval.')
            return redirect('home')
    else:
        form = PetMemorialForm()

    return render(request, 'petmemorial/create_memorial.html', {'form': form})
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


