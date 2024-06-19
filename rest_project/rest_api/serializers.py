from rest_framework import serializers

from . models import Planet


from django.contrib.auth.models import User

class PlanetSerializer(serializers.ModelSerializer):
    
    class Meta: # tells us what will be serialized
        
        model = Planet # model which it is based on 
        
        fields = ['id','name','size','fact'] # fields which will be included
        
        

class RegisterationSerializer(serializers.ModelSerializer):
    # This is a class for creating new users
    
    password2 = serializers.CharField(style={'input_type:' 'password'},write_only=True)
    
    # The password is only written, it is not shown 
    
    class Meta:
        
        model = User
        # It uses the User model
        fields = ['username','email','password','password2']
        # These are the fields needed
        extra_kwargs = { 'password': {'write_only':True}}
        # The password is only written, it is not shown        
    def save(self):
     # This function saves a new user
            
            user = User(
                
                username=self.validated_data['username'],
                # Get username from validated data
                email=self.validated_data['email'],
                # Get email from validated data
                
            )
            
            password=self.validated_data['password']
            # Get password from the validated data
            password2=self.validated_data['password2']
            # Get password2 from the validated data
            
            if password != password2:
                #check if password1 and password2 are not equal
                raise serializers.ValidationError({'password':'Sorry password not correct'})
                 # raise a validation error with the message
            user.set_password(password)
            # set the password
            
            user.save()
            # save the user to the database
            
            return user
            # Return the new user
            
            
        
