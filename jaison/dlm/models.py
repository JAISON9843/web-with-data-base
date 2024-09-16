from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    sname=models.CharField(max_length=50)
    semail=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    fee=models.DecimalField(decimal_places=0, max_digits=9)

    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)



