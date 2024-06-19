from django.db import models


from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Planet(models.Model):
    
    name = models.CharField(max_length=30) # name of the planet
    
    size = models.CharField(max_length=30) # size of the planet
    
    fact = models.CharField(max_length=150) # fact about the planet
    
    def __str__(self):
        
        return self.name # shows the objects by the name
    
    
@receiver(post_save,sender=User)
def generate_auth_token(sender, instance=None, created=False, **kwargs):
    
    if created:
        Token.objects.create(user=instance)
    
    
