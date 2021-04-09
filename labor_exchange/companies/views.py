from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Company
# Create your views here.


def index(request):
    companies = Company.objects.all()
    context = {
        "companies":companies
    }

    return render(request,"companies/index.html",context)

def add(request):
    if request.method == "POST":
        name = request.POST["name"]
        position  = request.POST["position"]
        income =  float(request.POST["income"])
        available = request.POST["available"]

        if available == "Yes":
            available = 1
        else:
            available = 0
        
        # Creating 
        company = Company.objects.create(name = name, position = position,income = income,available = available)



        return redirect("index")
    else:
        return render(request,"companies/add.html")
   
