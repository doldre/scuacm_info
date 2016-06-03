from django.db import models

# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=200)
    stu_id = models.CharField(unique=True, max_length=200, primary_key=True)
    cf_id = models.CharField(max_length=200)
    bc_id = models.CharField(max_length=200)
    soj_id = models.CharField(max_length=200)
    score = models.IntegerField()