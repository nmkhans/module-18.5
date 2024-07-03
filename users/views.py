from django.shortcuts import render, redirect
from .forms import RegistrationForm, ProfileEditForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_register(req):
  if not req.user.is_authenticated:
    if req.method == 'POST':
      form = RegistrationForm(req.POST)

      if form.is_valid():
        form.save()
        messages.success(req, 'Account created. Login to continue.')
        return redirect('user-login-page')
    else:
      form = RegistrationForm()

    return render(req, 'users/user_registration.html', {'form': form})
  else:
    return redirect('user-profile-page')

def user_login(req):
  if not req.user.is_authenticated:
    if req.method == 'POST':
      form = AuthenticationForm(req, req.POST)

      if form.is_valid():
        cd = form.cleaned_data
        username = cd['username']
        password = cd['password']

        user = authenticate(username = username, password = password)

        if user is not None:
          login(req, user)
          messages.success(req, 'Login successfull.')
          return redirect('user-profile-page')
    else:
      form = AuthenticationForm()
    return render(req, 'users/user_login.html', {'form': form})
  else:
    return redirect('user-profile-page')
  
@login_required
def user_logout(req):
  logout(req)
  messages.warning(req, 'Logut successfull')
  return redirect('home-page')
  
@login_required
def user_profile(req):
  return render(req, 'users/user_profile.html')

@login_required
def user_profile_edit(req):
  if req.method == 'POST':
    form = ProfileEditForm(req.POST, instance = req.user)

    if form.is_valid():
      form.save()
      messages.success(req, 'Profile updated')
      return redirect('user-profile-page')
  else:
    form = ProfileEditForm(instance = req.user)

  return render(req, 'users/user_profile_edit.html', {'form': form})

@login_required
def user_change_password(req):
  if req.method == 'POST':
    form = PasswordChangeForm(req.user, req.POST)

    if form.is_valid():
      form.save()
      update_session_auth_hash(req, form.user)
      messages.success(req, 'Password changed.')
      return redirect('user-profile-page')
  else:
    form = PasswordChangeForm(req.user)

  return render(req, 'users/user_change_password.html', {'form': form})

@login_required
def user_change_password_two(req):
  if req.method == 'POST':
    form = SetPasswordForm(req.user, req.POST)

    if form.is_valid():
      form.save()
      update_session_auth_hash(req, form.user)
      messages.success(req, 'Password changed')
      return redirect('user-profile-page')
  else:
    form = SetPasswordForm(req.user)

  return render(req, 'users/user_change_password.html', {'form': form})