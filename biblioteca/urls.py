from django.urls import path
from .views import indexPage, registro, login, adminHome

urlpatterns = [
    path('', indexPage),
    path('registro', registro),
    path('login', login),
    path('adminHome', adminHome)
]