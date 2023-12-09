from django.shortcuts import render, redirect
from django.contrib import auth


def index(request):
    pass

def register(request):
    #if request.method == 'POST':
    return render(request, 'parkapp/register.html')

def register_cuckold(reqiest):
    pass

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