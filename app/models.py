from django.db import models

# Create your models here.
class School(models.Model):
    student=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
    sid=models.IntegerField()