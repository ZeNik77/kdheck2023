from django.urls import path
from parkapp.views import *


app_name = 'parkapp'

urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('register_admin', register_admin, name='register_admin'),
    path('register_cuckold', register_cuckold, name='register_cuckold'),
    path('login', login, name='login'),
    path('pizdec', pizdec, name='pizdec')
]