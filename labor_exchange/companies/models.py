from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    income = models.DecimalField(max_digits=10,decimal_places=2)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.name



