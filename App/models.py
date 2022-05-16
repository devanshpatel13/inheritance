from django.db import models

# Create your models here.



class School(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField()
    address = models.CharField(max_length=100)
    age =models.IntegerField()
    class Meta:
        abstract = True
        ordering = ['name']


class Student(School):
    roll_no = models.IntegerField()
    std = models.IntegerField()

class Teacher(School):
    salary= models.IntegerField()
    subj = models.CharField(max_length=20)








