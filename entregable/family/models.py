from django.db import models

class family(models.Model):
    name = models.CharField(max_length=100)
    age = models.FloatField()
    study = models.BooleanField()
