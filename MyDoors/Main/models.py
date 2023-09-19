
from django.db import models

class Shape(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Molding(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Portal(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

class Door(models.Model):
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE, related_name='door_shapes')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='door_colors')
    molding = models.ForeignKey(Molding, on_delete=models.CASCADE, related_name='door_molding')
    portal = models.ForeignKey(Portal, on_delete=models.CASCADE, related_name='door_portal')

    def __str__(self):
        return f"Door - Shape: {self.shape}, Color: {self.color}, Molding: {self.molding}, Portal: {self.portal}"
