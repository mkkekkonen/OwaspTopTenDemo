from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

import ui.views as views

urlpatterns = [
  path('login/', views.loginView, name='login'),
  path('logout/', LogoutView.as_view(next_page='/')),
  path('register/', views.registerView, name='register'),
  path('horses/', views.horsesListView, name='horses_list'),
  path('horse/', views.addHorseView, name='add_horse'),
  path('horse/<int:horse_id>/', views.editHorseView, name='edit_horse')
]
