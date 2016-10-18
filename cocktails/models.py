from django.db import models

# Create your models here.
class Ingredient(models.Model):

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    desc = models.TextField()

    def post(self):
        self.save()

class Cocktail(models.Model):
    
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    directions = models.TextField()
    desc = models.TextField()
    
    def post(self):
        self.save() 
        
    def __str__(self):
        return self.name