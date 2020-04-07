from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request istek,  response sitenin vediği cevap


def index(request):
  #  return HttpResponse('<h1>hello</h1>')
  return render(request, 'pages/index.html')



def about(request):
    return render(request, 'pages/about.html')


def registerindex(request):
    return render(request, 'pages/registerindex.html')

def gamepage(request):
    return render(request, 'pages/gamepage.html')
