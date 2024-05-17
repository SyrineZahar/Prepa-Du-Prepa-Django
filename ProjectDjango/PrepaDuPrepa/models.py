from django.db import models

# Create your models here.

class user(models.Model):
    userId= models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    email = models.EmailField(max_length=100)  
    password = models.CharField(max_length=50) 
    role = models.CharField(max_length=8) 

class course(models.Model):
    courseId= models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    level = models.IntegerField()
    subject=models.CharField(max_length=7)