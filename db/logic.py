# -*- coding: utf-8 -*-

from db.models import Horse


def get_all_horses():
  return Horse.objects.all()


def add_horse(validated_data):
  name = validated_data['name']
  date_of_birth = validated_data['date_of_birth']
  gender = validated_data['gender']
  breed = validated_data['breed']
  color = validated_data['color']

  extra_info = validated_data.get('extra_info')

  return Horse.objects.create(
    name=name,
    date_of_birth=date_of_birth,
    gender=gender,
    breed=breed,
    color=color,
    extra_info=extra_info,
  )
