from django.db import models


class Horse(models.Model):
  G_STALLION = 's'
  G_MARE = 'm'
  G_GELDING = 'g'

  GENDER_CHOICES = (
    (G_STALLION, 'stallion'),
    (G_MARE, 'mare'),
    (G_GELDING, 'gelding'),
  )

  B_STANDARDBRED = 'sb'
  B_FRENCH_TROTTER = 'ft'
  B_RUSSIAN_TROTTER = 'rt'
  B_FINN_HORSE = 'fh'
  B_NORTH_SWEDISH_HORSE = 'nsh'
  B_SHETLAND_PONY = 'sp'
  B_GOTLAND_PONY = 'gp'

  BREED_CHOICES = (
    (B_STANDARDBRED, 'Standardbred'),
    (B_FRENCH_TROTTER, 'French trotter'),
    (B_RUSSIAN_TROTTER, 'Russian trotter'),
    (B_FINN_HORSE, 'Finn horse'),
    (B_NORTH_SWEDISH_HORSE, 'North Swedish horse'),
    (B_SHETLAND_PONY, 'Shetland pony'),
    (B_GOTLAND_PONY, 'Gotland pony'),
  )

  C_CHESTNUT = 'c'
  C_BAY = 'ba'
  C_BLACK = 'bl'
  C_GRAY = 'g'
  C_PINTO = 'p'

  COLOR_CHOICES = (
    (C_CHESTNUT, 'chestnut'),
    (C_BAY, 'bay'),
    (C_BLACK, 'black'),
    (C_GRAY, 'gray'),
    (C_PINTO, 'pinto'),
  )

  name = models.CharField(max_length=200)
  date_of_birth = models.DateField()

  gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
  breed = models.CharField(max_length=3, choices=BREED_CHOICES)
  color = models.CharField(max_length=2, choices=COLOR_CHOICES)

  extra_info = models.TextField(null=True, blank=True)

