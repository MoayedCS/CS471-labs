from django.db import models

# Create your models here.
class Address((models.Model)):
    city = models.CharField(max_length=50)
    def __str__(self):
        return self.city

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.ForeignKey(Address,on_delete=models.CASCADE)