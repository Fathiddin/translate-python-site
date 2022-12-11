from django.db import models

# Create your models here.

class List(models.Model):
    uzb = models.CharField(max_length=200)
    eng = models.CharField(max_length=200)
    
    def __str__(self):
        return (self.uzb)