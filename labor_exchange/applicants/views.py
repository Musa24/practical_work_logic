from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Applicants
from companies.models import Company


def create(request):
    if request.method == "POST":
        firstName = request.POST["firstName"]
        lastName  = request.POST["lastName"]
        age       =  int(request.POST["age"])
        education  = request.POST["education"]
        experience = request.POST["experience"]
        gender     = request.POST["gender"]
        computer     = request.POST["ability"]



        if computer == "YES":
            computer = 1
        else:
            computer = 0
        
        applicant = Applicants.objects.create(firstName = firstName,lastName = lastName, age = age, education = education , experience = experience , gender = gender , computer = computer  )

        return redirect("applicants")
    else:

        companies = Company.objects.filter(available = True)

        return  render(request,"applicants/create.html")

def applicants(request):
    applicants = Applicants.objects.all()

    context = {
        "applicants":applicants
    }

    return  render(request,"applicants/applicants.html",context)

def questions(request):
    if request.method == "POST":
        experience = request.POST["experience"]
        experience3= request.POST["experience3"]
        education  = request.POST["education"]
        income =  request.POST["income"]

        applicants = Applicants.objects.filter(experience = experience)

        qn2  = False
        qn3 = False
        qn4 = False

        if education != "":
            counts  = Applicants.objects.filter(education=education).count()
            qn2 = True
        
        if experience3 != "":
            applicant3 = Applicants.objects.filter(experience = experience)
            qn4 = True
            
        # Qn 3
        if income != "":
            income = float(income)
            companies_income = Company.objects.filter(income__gte = income)
            qn3 = True


        context = {
            "applicants":applicants,
            "counts":{
                "qn2":qn2,
                "counts":counts
            }  ,
             "income":{
                "qn3":qn3,
                "companies":companies_income
            } , 
             "experience":{
                "qn4":qn4,
                "applicants":applicant3
            }  
        }

        return render(request,"applicants/questions.html",context)
    return render(request,"applicants/questions.html")


