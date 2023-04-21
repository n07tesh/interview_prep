from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from app import models
class TaskCreationSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'