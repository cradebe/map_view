from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect

# Create your views here.
from user_details.forms import UserSignUpForm, UserProfileForm, UserUpdateForm


@login_required
@transaction.atomic
def profile_view(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        user_profile_form = UserProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        user_profile_form = UserProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': user_profile_form})


def signup_view(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'successfully created for {username}')
            return redirect('profile')
    else:
        form = UserSignUpForm()

    return render(request, 'registration/signup.html', {'form': form})
