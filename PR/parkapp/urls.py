from django.urls import path
from . import views
app_name = 'parkapp'

urlpatterns = [
    path('register', views.register, name='register'),
    path('register_admin', views.register_admin, name='register_admin')
]