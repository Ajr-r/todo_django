from django.db import models

# Create your models here.
class Task_r(models.Model):
    title=models.CharField(max_length=50,unique=True)
    desc=models.TextField()
    priority=models.CharField(max_length=10)
    user=models.CharField(max_length=10,blank=False)