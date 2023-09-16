from django.db import models

class Doors(models.Model):
    shape = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    molding = models.CharField(max_length=255)
    portal = models.CharField(max_length=255)