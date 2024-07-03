from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
  first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
  first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
  email = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
  
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']

class ProfileEditForm(UserChangeForm):
  password = None
  first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
  first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True}))
  email = forms.CharField(label='Email address', widget=forms.TextInput(attrs={'required': True}))

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']