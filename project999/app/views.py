from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import itemSerializer
from rest_framework import serializers
from rest_framework import status
from .models import item
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['GET'])
def Apiview(request):
    api_urls = {
        
        'Add': '/create',
        
    }
 
    return Response(api_urls)
@api_view(['POST'])
def add_items(request):
    items = itemSerializer(data=request.data)
 
    # validating for already existing data
    if item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if items.is_valid():
        items.save()
        return Response(items.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)