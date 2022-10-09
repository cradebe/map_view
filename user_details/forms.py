from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from user_details.models import Profile


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserProfileForm(forms.ModelForm):
    phone_number = forms.CharField()
    address = forms.CharField()

    class Meta:
        model = Profile
        fields = ['phone_number', 'address']
