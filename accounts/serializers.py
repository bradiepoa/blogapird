from rest_framework import serializers
from .models import User
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model=User
        fields = ['email','first_name','last_name','password','password2']
    
    def validate(self, attrs):
        password = attrs.get('password','')
        password2 = attrs.get('password2','')
        if password != password2:
            raise serializers.ValidationError("Password do not match please!")
        return attrs
    
    def create(self,validate_data):
        user=User.objects.create_user(
            email=validate_data['email'],
            first_name=validate_data.get('first_name'),
            last_name=validate_data.get('last_name'),
            password=validate_data.get('password')
        )
        return user
    

