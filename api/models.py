from django.db import models

# Create your models here.
class Employee(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  date_of_birth = models.DateField()
  salary = models.DecimalField(max_digits=7, decimal_places=2)