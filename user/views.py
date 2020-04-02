from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username,password=password)

    if user is not None:
      auth.login(request, user)
      messages.add_message(request, messages.SUCCESS,'Oturum açıldı.')
      return redirect('index')
    else:
      messages.add_message(request,messages.ERROR,'Kulllanıcı adı veya Parola yanlış.')
      return redirect('index')

  else:
    return render(request, 'user/login.html')




def register(request):
  if request.method == 'POST':
    
    username  = request.POST['username']
    email  = request.POST['email']
    password  = request.POST['password']
    repassword  = request.POST['repassword']

    if password == repassword:
      if User.objects.filter(username = username).exists():
        messages.add_message(request,messages.WARNING,'Bu kullanıcı adı daha önce alınmış.')
        return redirect('registerindex')
      else: #kayit işlemi
        user = User.objects.create_user(username=username, password=password,email=email,last_name=0)
        user.save()
        messages.add_message(request,messages.SUCCESS,'Hesap oluşturuldu')
        return redirect('index')
    else:
      messages.add_message(request,messages.WARNING,'Parolalar eşleşmiyor.')
      return redirect('registerindex')
  else:
    return render(request, 'user/registerindex.html')

def logout(request):
  auth.logout(request)
  messages.add_message(request,messages.SUCCESS,'Çıkış işlemi tamamlandı')
  return redirect('index')



def ranking_main(request):

  return render(request, 'user/ranking_main.html')