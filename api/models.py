from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=20,default='')
    clas = models.CharField(max_length=20,default='')
    result = models.CharField(max_length=20,default='')
    def __str__(self):
        return self.name