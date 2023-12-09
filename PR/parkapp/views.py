from django.shortcuts import render, redirect
from django.contrib import auth
from .models import *
from django.urls import reverse


def index(request):
    pass

def register(request):
    #if request.method == 'POST':
    return render(request, 'parkapp/register.html')

def register_cuckold(request):
    if request.method == 'POST':
        user = request.user
        admins = User.objects.filter(rights=2)
        if user in admins:
            name = request.POST.get('name')
            password = request.POST.get('password')
            park_id = request.POST.get('parkid')
            User.objects.create(name=name, password=password, park_id=park_id)
            return redirect(reverse('parkapp:login'))
        else:
            return render('parkapp/poshelvon.html')

def register_admin(request):
    return render(request, 'parkapp/register_admin.html')

def login(request):
    if request.method == 'POST':
        card_name = request.POST.get('card_name')
        password = request.POST.get('password')
        user = auth.authenticate(card_name=card_name, password=password)
        if user:
            auth.login(request, user)
            return redirect('/')
    return render(request, 'parkapp/login.html')