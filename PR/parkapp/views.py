from django.shortcuts import render, redirect
from django.contrib import auth
from .models import *
from django.urls import reverse

from django.shortcuts import render, redirect, HttpResponseRedirect


def index(request):

    return render(request, 'parkapp/index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        card_num = request.POST.get('card_num')
        card_period = request.POST.get('card_period')
        card_cvv = request.POST.get('card_cvv')
        user_password = request.POST.get('user_password')
        print(username, card_num, card_period, card_cvv, user_password)

        User.objects.create(username=username, card_num=card_num, card_period=card_period, card_cvv=card_cvv, password=user_password)
        return HttpResponseRedirect(reverse('parkapp:login'))

    else:
        return render(request, 'parkapp/register.html')

def register_cuckold(request):
    if request.method == 'POST':
        user = request.user
        admins = User.objects.filter(rights=2)
        if user in admins:
            username = request.POST.get('username')
            password = request.POST.get('password')
            park_id = request.POST.get('parkid')
            User.objects.create(username=username, password=password, park_id=park_id)
            return HttpResponseRedirect(reverse('parkapp:login'))
        else:
            return render('parkapp/poshelvon.html')

def register_admin(request):
    if request.method == 'POST':
        admin_fio = request.POST.get('admin_fio')
        admin_password = request.POST.get('admin_passord')
        rights = 2
        User.objects.create(username=admin_fio, password=admin_password, rights=rights)
        return HttpResponseRedirect(reverse('parkapp:login'))
    else:
        return render(request, 'parkapp/register_admin.html')

def login(request):
    if request.method == 'POST':
        card_username = request.POST.get('card_username')
        password = request.POST.get('password')
        user = auth.authenticate(card_username=card_username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('parkapp:index'))
    return render(request, 'parkapp/login.html')