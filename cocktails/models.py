from django.db import models

# Create your models here.
class Ingredients(models.Model):
    
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    desc = models.TextField()
    
class Cocktail(models.Model):
    
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    amts = models.DecimalField(max_digits=5,decimal_places=2)
    directions = models.TextField()
    desc = models.TextField()
    
    def publish(self):
        self.save()
        
    def __str__():
        return self.name
