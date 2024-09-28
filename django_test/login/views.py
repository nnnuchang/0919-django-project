from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/operation/show')
    else:
        return HttpResponseRedirect('/login')

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/operation/show')
    
    username = request.POST.get('account', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username = username, password = password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/operation/show')
    else:
        return render(request, 'login.html', locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login')