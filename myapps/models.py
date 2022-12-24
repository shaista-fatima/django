from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200)
    feedback=models.CharField(max_length=300)
    def __str__(self):
        return self.name

