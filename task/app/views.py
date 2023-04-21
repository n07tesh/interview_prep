from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import authtoken
from rest_framework import status
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from app import serializers
from rest_framework.authtoken.models import Token

from app.models import User

class Task(viewsets.GenericViewSet):
    # permission_classes = [IsAuthenticated]
    
    @action(detail=False,methods=['post'])
    def user_creation(self,request):
        data = request.data
        files = request.FILES['file']
        try:
            User.objects.create(**data)
            return Response(True,status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response(str(ex),status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=False,methods=['get'])
    def get_all_creation(self,request):
        user_obj = User.objects.all()
        serializer = serializers.TaskCreationSerializer(user_obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



    

    
        
            


