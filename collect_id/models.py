from django.db import models

# Create your models here.
from .get_rating import get_bc_rating, get_cf_rating
class Info(models.Model):
    name = models.CharField(max_length=200, null=False)
    stu_id = models.CharField(unique=True, max_length=200, primary_key=True)
    cf_id = models.CharField(max_length=200, null=True)
    bc_id = models.CharField(max_length=200, null=True)
    soj_id = models.CharField(max_length=200, null=True)
    cf_rating = models.IntegerField(default=0)
    bc_rating = models.IntegerField(default=0)
    cf_score = models.IntegerField(default=0)
    bc_score = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    def update_score(self):
        self.cf_rating = int(get_cf_rating(self.cf_id))
        self.bc_rating = int(get_bc_rating(self.bc_id))
        t = int(max(0, (self.cf_rating - 1200) / 80))
        self.cf_score = t * t
        t = int(max(0, (self.bc_rating - 1250) / 90))
        self.bc_score = t * t
        self.score = self.bc_score + self.cf_score
        self.save()