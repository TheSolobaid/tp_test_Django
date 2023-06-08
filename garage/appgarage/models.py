from django.db import models

# Create your models here.
class auto(models.Model):
    model = models.CharField(max_length=255)
    marque = models.CharField(max_length=255)
    date_achat = models.DateField(blank=True, null = True)
    nombre_place = models.IntegerField()
    description = models.TextField(null = True, blank = True)
    longeur = models.IntegerField()
    clim = models.BooleanField(blank=True)