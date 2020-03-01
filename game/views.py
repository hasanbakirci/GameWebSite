from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def game1(request):
  return render(request, 'game/game1.html')
