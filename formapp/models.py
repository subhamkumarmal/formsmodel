from django.db import models
from django.forms import forms

# Create your models here.

class Students(models.Model):
    students_id=models.AutoField
    students_name=models.CharField(max_length=40,default="")
    students_age=models.IntegerField()
    students_email=models.EmailField(default="")
    students_password=models.CharField(max_length=20,default="")


    class meta:
        db_table='StudentsDetails';