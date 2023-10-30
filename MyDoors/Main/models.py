from django.db import models
import json


class Door(models.Model):
    collection = models.CharField(max_length=100, default='Classic', null=False)
    shape = models.CharField(max_length=100, default='default', null=False)
    portal = models.CharField(max_length=100, default='default', null=False)
    bevel = models.CharField(max_length=100, default='default', null=False)
    molding = models.CharField(max_length=100, default='default', null=False)
    color = models.CharField(max_length=100, default='default', null=False)
    image = models.ImageField(upload_to='door_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=False)

    def __str__(self):
        return self.collection + self.shape + self.portal + self.bevel + self.molding + self.color + str(self.price)

    def get_image(self):
        return self.image.name




class Basket(models.Model):
    code = models.CharField(max_length=512)
    door = models.ForeignKey(Door, on_delete=models.CASCADE)
    count = models.DecimalField(max_digits=5, decimal_places=0, default=1, null=False)

    def __str__(self):
        return str(self.code) + str(self.door) + str(self.count)
