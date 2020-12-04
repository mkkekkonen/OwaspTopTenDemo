# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from db.models import Horse
import db.logic as DbLogic

from ui.forms import AddEditHorseForm


OPTIONS = {
  'gender_options': Horse.GENDER_CHOICES,
  'breed_options': Horse.BREED_CHOICES,
  'color_options': Horse.COLOR_CHOICES,
}


def horsesListView(request):
  if request.method == 'GET':
    logged_in = request.user.is_authenticated
    flash_error = request.session.pop('flash_error', None)

    horses = DbLogic.get_all_horses()

    return render(request, 'data/horseList.html', {
      'horses': horses,
      'logged_in': logged_in,
      'flash_error': flash_error,
    })


def addHorseView(request):
  if request.method == 'GET':
    return render(request, 'data/addEdit.html', {
      'logged_in': True,
      **OPTIONS,
    })

  elif request.method == 'POST':
    form = AddEditHorseForm(request.POST)

    if form.is_valid():
      try:
        horse = DbLogic.add_horse(form.cleaned_data)
      except Exception as e:
        return render(request, 'data/addEdit.html', {
          'flash_error': e,
          'logged_in': True,
          'form': form,
          **OPTIONS,
        })

      return redirect('/horses')

    return render(request, 'data/addEdit.html', {
      'logged_in': True,
      'form': form,
      **OPTIONS,
    })


def editHorseView(request, horse_id):
  if request.method == 'GET':
    try:
      horse = Horse.objects.get(pk=horse_id)
    except ObjectDoesNotExist:
      request.session['flash_error'] = 'Horse with the ID {} does not exist.'.format(horse_id)
      return redirect('/horses')

    form = AddEditHorseForm(initial={
      'name': horse.name,
      'date_of_birth': horse.date_of_birth,
      'gender': horse.gender,
      'breed': horse.breed,
      'color': horse.color,
      'extra_info': horse.extra_info,
    })

    return render(request, 'data/addEdit.html', {
      'logged_in': True,
      'editing': True,
      'form': form,
      **OPTIONS,
    })
  
  elif request.method == 'POST':
    form = AddEditHorseForm(request.POST)

    horse = None
    try:
      horse = Horse.objects.get(pk=horse_id)
    except ObjectDoesNotExist:
      return render(request, 'data/addEdit.html', {
        'flash_error': 'Horse with the ID {} does not exist.'.format(horse_id),
        'logged_in': True,
        'editing': True,
        'form': form,
        **OPTIONS,
      })

    if form.is_valid():
      try:
        horse.name = form.cleaned_data['name']
        horse.date_of_birth = form.cleaned_data['date_of_birth']
        horse.gender = form.cleaned_data['gender']
        horse.breed = form.cleaned_data['breed']
        horse.color = form.cleaned_data['color']
        horse.extra_info = form.cleaned_data.get('extra_info')
        horse.save()
      except Exception as e:
        return render(request, 'data/addEdit.html', {
          'flash_error': e,
          'logged_in': True,
          'editing': True,
          'form': form,
          **OPTIONS,
        })

      return redirect('/horses')

    return render(request, 'data/addEdit.html', {
      'logged_in': True,
      'editing': True,
      'form': form,
      **OPTIONS,
    })
