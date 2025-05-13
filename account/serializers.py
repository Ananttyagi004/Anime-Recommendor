from django.contrib.auth.models import User
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
    
    def create(self, validated_data):
        password_hash=User.objects.create_user(username=validated_data['username'])
        password_hash.set_password(validated_data['password'])
        password_hash.save()
        return password_hash
    
class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=20)
    password=serializers.CharField(max_length=20)