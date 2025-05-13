from rest_framework import serializers
from .models import *



class AniListSearchSerializer(serializers.Serializer):
    search = serializers.CharField(max_length=255, required=True)
    genre = serializers.CharField(max_length=255, required=False)

class PrefrenceSerializer(serializers.Serializer):
    prefrence = serializers.ListField(
        child=serializers.CharField(max_length=255),
        required=True
    )