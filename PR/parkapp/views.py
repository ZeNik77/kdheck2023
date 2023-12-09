from django.shortcuts import render, redirect
from django.contrib import auth
from parkapp.models import *
from django.urls import reverse

from django.shortcuts import render, redirect, HttpResponseRedirect

'''
def zapolnit():
    with open('./123.txt', 'r', encoding='utf-8') as f:
        s = [el.strip().split('\t') for el in f.readlines()]
    s2 = []
    for el in s:
        s2.append([el[3], el[5]])
    print(s2)
'''

def index(request):
    return render(request, 'parkapp/index.html', {'parking': Parking.objects.all()})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        card_num = request.POST.get('card_num')
        card_period = request.POST.get('card_period')
        card_cvv = request.POST.get('card_cvv')
        user_password = request.POST.get('user_password')
        # print(username, card_num, card_period, card_cvv, user_password)
        User.objects.create(username=username, card_num=card_num, card_period=card_period, card_cvv=card_cvv, password=user_password)
        return HttpResponseRedirect(reverse('parkapp:login'))

    else:
        return render(request, 'parkapp/register.html')

def register_cuckold(request):
    if request.method == 'POST':
        user = request.user
        print(user)
        admins = User.objects.filter(rights=2)
        if user in admins:
            username = request.POST.get('username')
            password = request.POST.get('password')
            park_id = request.POST.get('park_id')
            User.objects.create(username=username, password=password, park_id=park_id, rights=1)
            return HttpResponseRedirect(reverse('parkapp:login'))
        else:
            return render(request, 'parkapp/poshelvon.html')
    return render(request, 'parkapp/register_cuckold.html')

def register_admin(request):
    if request.method == 'POST':
        user = request.user
        print(user)
        admins = User.objects.filter(rights=2)
        if user in admins:
            username = request.POST.get('username')
            password = request.POST.get('password')
            User.objects.create(username=username, password=password, rights=2)
            return HttpResponseRedirect(reverse('parkapp:login'))
        else:
            return render(request, 'parkapp/poshelvon.html')
    return render(request, 'parkapp/register_admin.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(reverse('parkapp:index'))
        except:
            return render(request, 'parkapp/login.html', {'error': 'СОСИ'})
    else:
        return render(request, 'parkapp/login.html')


