from rest_framework import serializers

from . models import Planet

class PlanetSerializer(serializers.ModelSerializer):
    
    class Meta: # tells us what will be serialized
        
        model = Planet # model which it is based on 
        
        fields = ['id','name','size','fact'] # fields which will be included