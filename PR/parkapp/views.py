from django.shortcuts import render, redirect
from django.contrib import auth
from parkapp.models import *
from django.urls import reverse
import random
import datetime

from django.shortcuts import render, redirect, HttpResponseRedirect


def index(request):
    if request.method == 'POST':
        if 'create_park' in request.POST:
            user = request.user
            park_id = request.POST.get('park_id')
            parkings = Parking.objects.filter(pk=park_id)
            if parkings:
                parking = parkings[0]
                print(park_id)
                starttime = datetime.datetime.now()
                Reciept.objects.create(parking_id=parking, user_id=user, start_time=starttime, finish_time=starttime)
        elif 'end_park' in request.POST:
            reciept_id = request.POST.get('end_park')
            reciept = Reciept.objects.get(pk=reciept_id)
            reciept.finish_time = datetime.datetime.now()
            # print(reciept.parking_id)
            parking = Parking.objects.get(pk=reciept.parking_id.pk)
            dif = (reciept.finish_time.replace(tzinfo=None) - reciept.start_time.replace(tzinfo=None))
            dif = dif.total_seconds()
            reciept.final_price = int(parking.price_per_minute * dif // 60)
            print(reciept.final_price)
            reciept.save()

    reciepts = Reciept.objects.filter(user_id=request.user, final_price=-1)
    return render(request, 'parkapp/index.html', {'parking': Parking.objects.all(), 'reciepts': reciepts})


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


def pizdec(request):
    return render(request, 'parkapp/pizdec.html')