from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.

def game1(request):
  if request.method == 'POST':
    
    
    last_name  = request.POST['puan']
    username =  request.user.username
    User.objects.filter(username= username ).update(last_name=last_name)
    messages.add_message(request,messages.SUCCESS,'Puan başarıyla güncellendi.')
        
    return render(request, 'pages/gamepage.html') 
  else:
    messages.add_message(request,messages.WARNING,'Bir hata oluştu.')
    return render(request, 'game/gamepage.html') 

  
  
