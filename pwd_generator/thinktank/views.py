from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

#def home(request):
 #   return HttpResponse('hello there friends!!')


def about(request):
    return render(request,'thinktank/about.html')
def home(request):
    return render(request,'thinktank/home.html')


def password(request):
   
    
    characters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('upper'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('@#%^&*()!'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    length=int(request.GET.get('length'))
    thepassword=''
    for x in range(length):
        thepassword+=random.choice(characters)
    return render(request,'thinktank/password.html',{'password':thepassword})