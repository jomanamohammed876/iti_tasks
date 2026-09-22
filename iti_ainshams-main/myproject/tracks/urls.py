from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', alltracks),
    path('id/',gettrack),
    path('insert/',inserttrack),
    path('update/<int:id>',updatetrack, name='updatetrack'),
    path('delete/<int:id>',deletetrack, name='deletetrack'),
]
