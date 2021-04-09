from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('applicants/add/', views.create, name="create"),
    path("applicants/",views.applicants, name="applicants"),
    path("",views.questions, name="questions")
]
