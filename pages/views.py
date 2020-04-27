from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
# request istek,  response sitenin vediği cevap




def index(request):
  #  return HttpResponse('<h1>hello</h1>')
    queryset = User.objects.all().order_by('-last_name')[:10]
     
    return render(request, 'pages/index.html', {"object_list": queryset})
  
def about(request):
    return render(request, 'pages/about.html')


def registerindex(request):
    return render(request, 'pages/registerindex.html')

def gamepage(request):
    return render(request, 'pages/gamepage.html')


def siralama(request):
    return render(request, 'pages/siralama.php')
