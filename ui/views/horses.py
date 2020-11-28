from django.shortcuts import render

from ui.models import Horse

def horsesListView(request):
  if request.method == 'GET':
    logged_in = request.user.is_authenticated

    horses = Horse.objects.all()

    return render(request, 'data/horseList.html', { 'horses': horses, 'logged_in': logged_in })
