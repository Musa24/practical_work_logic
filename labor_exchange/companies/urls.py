from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('companies/add/', views.add, name="add"),
    path("companies",views.index, name="index")
 
]
