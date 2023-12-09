from django.urls import path
from . import views
app_name = 'parkapp'

urlpatterns = [
    path('register', views.register, name='register'),
    path('register_admin', views.register_admin, name='register_admin'),
    path('register_cuckold', views.register_cuckold, name='register_cuckold'),
    path('login', views.login, name='login'),
]