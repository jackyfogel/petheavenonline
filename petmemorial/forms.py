from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PetMemorial

class EmailRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def save(self, commit=True):
        email = self.cleaned_data['email']
        base_username = email.split('@')[0]
        username = base_username
        counter = 1

        # 💣 Make sure username is unique (jacky, jacky1, jacky2...)
        while User.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1

        user = super().save(commit=False)
        user.username = username
        user.email = email

        if commit:
            user.save()
        return user
class PetMemorialForm(forms.ModelForm):
    class Meta:
        model = PetMemorial
        exclude = ['user', 'status', 'slug']
