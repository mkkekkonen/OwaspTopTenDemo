from django.shortcuts import render

def helloView(request):
  return render(request, 'hello/hello.html')
