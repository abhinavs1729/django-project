from django.db import models

# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
    date = models.DateField()
    objects = models.Manager()

class blogss(models.Model):
    Title = models.CharField(max_length=20)
    Content = models.CharField(max_length=1000)
    objects = models.Manager()