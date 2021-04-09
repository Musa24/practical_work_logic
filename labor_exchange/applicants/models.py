from django.db import models
from companies.models import Company

class Applicants(models.Model):
    company   = models.ForeignKey(Company,on_delete=models.DO_NOTHING,default=None)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    age  = models.IntegerField()
    education = models.CharField(max_length=200)
    experience = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    computer = models.BooleanField(default=False)

    def __str__(self):
        return self.firstName
