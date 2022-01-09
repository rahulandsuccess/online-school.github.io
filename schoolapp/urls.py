from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.base,name='base'),
    path("login",views.login,name='login'),
    path("result/",views.result,name='result'),
    path("attendence",views.attendence,name='attendence')
]
