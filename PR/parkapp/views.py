from django.shortcuts import render, redirect

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
    pass

def login_cuckold(request):
    pass

def login_admin(request):
    pass
