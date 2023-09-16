from django.db import models

class Doors(models.Model):
    SHAPE_CHOICES = [
        ('none', 'None'),
    ]

    COLOR_CHOICES = [
        ('none', 'None'),
    ]

    MOLDING_CHOICES = [
        ('none', 'None'),
    ]

    PORTAL_CHOICES = [
        ('none', 'None'),
    ]

    shape = models.CharField(max_length=100, choices=SHAPE_CHOICES)
    color = models.CharField(max_length=100, choices=COLOR_CHOICES)
    molding = models.CharField(max_length=100, choices=MOLDING_CHOICES)
    portal = models.CharField(max_length=100, choices=PORTAL_CHOICES)

    # Другие поля и методы модели...
