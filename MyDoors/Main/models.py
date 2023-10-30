from django.db import models


class Shape(models.Model):
    name = models.CharField(max_length=100, default='Default Shape', null=False)

    def __str__(self):
        return self.name


class Portal(models.Model):
    name = models.CharField(max_length=100)
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


class Bevel(models.Model):
    name = models.CharField(max_length=100)
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE, null=False)
    portal = models.ForeignKey(Portal, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


class Molding(models.Model):
    name = models.CharField(max_length=100)
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE)
    portal = models.ForeignKey(Portal, on_delete=models.CASCADE)
    bevel = models.ForeignKey(Bevel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100, default='Default Color', null=False)

    def __str__(self):
        return self.name


class Door(models.Model):
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE, null=False)
    portal = models.ForeignKey(Portal, on_delete=models.CASCADE, null=False)
    bevel = models.ForeignKey(Bevel, on_delete=models.CASCADE, null=False)
    molding = models.ForeignKey(Molding, on_delete=models.CASCADE, null=False)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to='door_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=False)

    def __str__(self):
        return "Форма : " + self.shape.name + "\n" + "Портал : " + self.portal.name + "\n" + "Фреза : " + \
            self.bevel.name + "\n" + "Молдинг : " + self.molding.name + "\n" + "Цвет : " + self.color.name + \
            "\n" + "Цена : " + str(round(self.price)) + " ₽"

    def get_image(self):
        return self.image.name


class Basket(models.Model):
    code = models.CharField(max_length=512)
    door = models.ForeignKey(Door, on_delete=models.CASCADE)
    count = models.DecimalField(max_digits=5, decimal_places=0, default=1, null=False)

    def __str__(self):
        return str(self.code) + str(self.door) + str(self.count)
