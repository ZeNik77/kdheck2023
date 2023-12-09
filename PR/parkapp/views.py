from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    #if request.method == 'POST':
    return render(request, 'parkapp/register.html')

def register_admin(request):
    return render(request, 'parkapp/register_admin.html')

#def register_