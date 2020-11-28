from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

import ui.views as views

urlpatterns = [
  path('login/', views.loginView, name='login'),
  path('logout/', LogoutView.as_view(next_page='/')),
  path('register/', views.registerView, name='register'),
  path('horses/', views.horsesListView, name='horses_list'),
]
