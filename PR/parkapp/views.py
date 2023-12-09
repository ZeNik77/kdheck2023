from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from parkapp.models import *

def index(request):
    render(request, 'parkapp/index.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        card_num = request.POST.get('card_num')
        card_period = request.POST.get('card_period')
        card_cvv = request.POST.get('card_cvv')
        user_password = request.POST.get('user_password')

        User.objects.create(name=name, card_num=card_num, card_period=card_period, card_cvv=card_cvv, password=user_password)
        return HttpResponseRedirect(reverse('parkapp:login'))

    else:
        return render(request, 'parkapp/register.html')

def register_couponer(request):
    admins = User.objects.filter(rights=2)
    if request.user in admins:


def register_admin(request):
    if request.method == 'POST':
        admin_fio = request.POST.get('admin_fio')
        admin_password = request.POST.get('admin_passord')
        rights = 2
        User.objects.create(name=admin_fio, password=admin_password, rights=rights)
        return HttpResponseRedirect(reverse('parkapp:login'))
    else:
        return render(request, 'parkapp/register_admin.html')

def login(request):
    pass

def login_couponer(request):
    pass

def login_admin(request):
    pass
