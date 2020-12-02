# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

from db.models import Horse
import db.logic as DbLogic

from ui.forms import AddEditHorseForm


def horsesListView(request):
  if request.method == 'GET':
    logged_in = request.user.is_authenticated

    horses = DbLogic.get_all_horses()

    return render(request, 'data/horseList.html', { 'horses': horses, 'logged_in': logged_in })


def addHorseView(request):
  options = {
    'gender_options': Horse.GENDER_CHOICES,
    'breed_options': Horse.BREED_CHOICES,
    'color_options': Horse.COLOR_CHOICES,
  }

  if request.method == 'GET':
    return render(request, 'data/addEdit.html', {
      'logged_in': True,
      **options,
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
          **options,
        })

      return redirect('/horses')

    return render(request, 'data/addEdit.html', {
      'logged_in': True,
      'form': form,
      **options,
    })
