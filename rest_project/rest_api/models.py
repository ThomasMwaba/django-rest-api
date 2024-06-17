from django.db import models

# Create your models here.

class Planet(models.Model):
    
    name = models.CharField(max_length=30) # name of the planet
    
    size = models.CharField(max_length=30) # size of the planet
    
    fact = models.CharField(max_length=50) # fact about the planet
    
    def __str__(self):
        
        return self.name # shows the objects by the name
    
    
