from django.shortcuts import render

from . models import Planet

from . serializers import PlanetSerializer


from . serializers import RegisterationSerializer

from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status

from rest_framework.authtoken.models import Token

# Create your views here.

@api_view(['GET','POST'])
def planet_list(request):
    
    if request.method == 'GET':
         # if the request is a GET request
        
        planets = Planet.objects.all() 
        # get all the Planet objects from the database
        
        serializer = PlanetSerializer(planets,many=True) 
        # serialize all the Planet objects into JSON format
        
        return Response(serializer.data) 
        # Return the serialized data in JSON format
    
    
    elif request.method == 'POST': 
    #If the request is a POST
        
        serializer = PlanetSerializer(data=request.data) 
        # Deserialize the  JSON data being sent into a Planet object
        
        if serializer.is_valid() :
        #If the deserialized data is valid
            
            serializer.save() 
            # save the new planet object to the database
            
            return Response(serializer.data) 
            # return the serialized data of the save object in JSON format


@api_view(['GET','PUT','DELETE'])
def planet(request,pk):
    
    try:
        planet = Planet.objects.get(id=pk)
        # get the planet where id = pk
        
    except:
        
        Planet.DoesNotExist()
        # if the planet doesn't exist
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
    # if the request is a GET request
        
        serializer = PlanetSerializer(planet)
        # serialize the Planet object into JSON format
        
        return Response(serializer.data)
         # return the serialized data of the save object in JSON format
    
    
    elif request.method == 'PUT':
    # if the request is a PUT request
        
        serializer = PlanetSerializer(planet,data=request.data) 
        # Deserialize the  JSON data being sent into a Planet object
        
        if serializer.is_valid() :
        #If the deserialized data is valid
            
            serializer.save() 
            # save the new planet object to the database
            
            return Response(serializer.data)
             # return the serialized data of the save object in JSON format
        
        
    elif request.method == 'DELETE':
    # If the request is a DELETE request
        
        planet.delete()
        
        # Delete the planet
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        # Return the HTTP 204 status code
        
        
        
@api_view(['POST'])
def register(request):
    
    if request.method == 'POST':
        # If the request is a POST request
        
        serializer = RegisterationSerializer(data=request.data)
        # serialize the incoming data
        
        data = {}
        # Empty dictionary to save reponses
        
        if serializer.is_valid():
            # if the serialized data is valid
            
            user = serializer.save()
            # save the user
            
            data['response'] = 'The user has been successfully registered'
            # save the reponse as 'user has been successfully' to be registered
            
            auth_token = Token.objects.get(user=user).key
            # get the token based on the user
            
            data['token'] = auth_token
            # return the token based on the user
            
            
            
        else:
            
            data = serializer.errors
            # save validation error in the data dictionary from serializer.py
        
        return Response(data)
        # Return the response based on data
            
            
        
        
        
        
    
    

        
        
    
