from django.db import models

# Create your models here.
class student1(models.Model):
    stuname = models.CharField(max_length=40)
    stuage = models.IntegerField()
    sturno = models.IntegerField()

    def __str__(self) :
        return f"Name {self.stuname} and age {self.stuage} and roll number is {self.sturno}"