# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):
  first_name = forms.CharField(label='First name', max_length=100)
  last_name = forms.CharField(label='Last name', max_length=100)
  email = forms.EmailField(label='Email', max_length=100)
  password = forms.CharField(label='Password', max_length=100)
  password_repeat = forms.CharField(label='Repeat password', max_length=100)

  def clean(self):
    cleaned_data = super().clean()

    password = cleaned_data.get('password')
    password_repeat = cleaned_data.get('password_repeat')

    if password != password_repeat:
      raise ValidationError('Passwords do not match!')


class LoginForm(forms.Form):
  username = forms.CharField(label='User name', max_length=100)
  password = forms.CharField(label='Password', max_length=100)


class AddEditHorseForm(forms.Form):
  name = forms.CharField(label='Name', max_length=200)
  date_of_birth = forms.DateField(label='Date of birth')
  gender = forms.CharField(label='Gender', max_length=1)
  breed = forms.CharField(label='Breed', max_length=3)
  color = forms.CharField(label='Color', max_length=2)
  extra_info = forms.CharField(label="Extra info (optional)", max_length=1000, required=False)
