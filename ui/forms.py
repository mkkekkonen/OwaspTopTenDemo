from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
  first_name = forms.CharField(label='First name', max_length=100, required=True)
  last_name = forms.CharField(label='Last name', max_length=100, required=True)
  email = forms.EmailField(label='Email', max_length=100, required=True)
  password = forms.CharField(label='Password', max_length=100, required=True)
  password_repeat = forms.CharField(label='Repeat password', max_length=100, required=True)

  def clean(self):
    cleaned_data = super().clean()

    password = cleaned_data.get('password')
    password_repeat = cleaned_data.get('password_repeat')

    if password != password_repeat:
      raise ValidationError('Passwords do not match!')


class LoginForm(forms.Form):
  username = forms.CharField(label='User name', max_length=100, required=True)
  password = forms.CharField(label='Password', max_length=100, required=True)
