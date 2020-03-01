from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):

  return render(request, 'user/login.html')

def register(request):

  return render(request, 'user/register.html')

def ranking(request):

  return render(request, 'user/ranking.html')

def ranking_main(request):

  return render(request, 'user/ranking_main.html')