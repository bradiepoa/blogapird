from rest_framework import serializers
from .models import User



class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model=User
        fields = ['email','first_name','last_name','password','password2']
    
    def validate(self, altrs):

        return super().validate(altrs)
    
    def create(self,validate_data):

        return super().create(validate_data)
    

