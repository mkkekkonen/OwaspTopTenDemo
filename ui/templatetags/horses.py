from django import template

from db.models import Horse

register = template.Library()

@register.simple_tag
def gender(gender_key):
  return [choice for choice in Horse.GENDER_CHOICES if choice[0] == gender_key][0][1]


@register.simple_tag
def breed(breed_key):
  return [choice for choice in Horse.BREED_CHOICES if choice[0] == breed_key][0][1]


@register.simple_tag
def color(color_key):
  return [choice for choice in Horse.COLOR_CHOICES if choice[0] == color_key][0][1]