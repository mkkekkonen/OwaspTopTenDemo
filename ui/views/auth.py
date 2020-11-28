from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from ui.forms import LoginForm, RegisterForm

def loginView(request):
  if request.method == 'GET':
    flash_success = request.session.get('flash_success')

    return render(request, 'auth/login.html', { 'flash_success': flash_success })

  elif request.method == 'POST':
    form = LoginForm(request.POST)

    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']

      user = authenticate(request, username=username, password=password)

      if user is not None:
        login(request, user)

        return redirect('/')

      else:
        return render(request, 'auth/login.html', {
          'flash_error': 'Wrong username/password combination',
          'form': form,
        })

    return render(request, 'auth/login.html', {
      'flash_error': 'Could not log in',
      'form': form,
    })

def helloView(request):
  logged_in = request.user.is_authenticated

  return render(request, 'hello/hello.html', { 'logged_in': logged_in })

def registerView(request):
  if request.method == 'GET':
    return render(request, 'auth/register.html')

  elif request.method == 'POST':
    form = RegisterForm(request.POST)

    if form.is_valid():
      first_name = form.cleaned_data['first_name']
      last_name = form.cleaned_data['last_name']
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']

      try:
        user = User.objects.create(
          username=email,
          email=email,
          first_name=first_name,
          last_name=last_name,
        )
        user.set_password(password)
        user.save()
      except Exception as e:
        return render(request, 'auth/register.html', { 'form': form, 'flash_error': e })

      request.session['flash_success'] = 'Registration successful!'

      return redirect('/login')

    return render(request, 'auth/register.html', { 'form': form })
