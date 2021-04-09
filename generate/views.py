from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generate/home.html',{'password':'sdflkjsdflkj7'})

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend('1234567890')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*')
    thepassword = ''
    password = ''
    for x in range(length):
        password += random.choice(characters)
    thepassword = password
    return render(request,'generate/password.html',{'password':thepassword})

def aboutus(request):
    return render(request,'generate/about_us.html')

def advise(request):
    return render(request,'generate/advise.html')