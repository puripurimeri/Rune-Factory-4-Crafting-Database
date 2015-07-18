from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=250, unique=True)
    category = models.CharField(max_length=250)
    subcategory = models.CharField(max_length=250)
    skilllvl = models.IntegerField(blank=True, null=True)
    sellvalue = models.IntegerField(blank=True, null=True)
    ingredient = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name
