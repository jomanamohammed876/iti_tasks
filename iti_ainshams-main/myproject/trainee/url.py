from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', alltrainee),
    path('id/',gettrainee),
    path('insert/',inserttrainee),
    path('update/<int:id>',updatetrainee,name='updatetrainee'),
    path('delete/<int:id>',deletetrainee,name='deletetrainee'),
]
