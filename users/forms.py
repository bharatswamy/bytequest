from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["fb_username"]  # Add fields as needed


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
    # class Meta:
    #     model = User
    #     fields = ["username", "password"]
