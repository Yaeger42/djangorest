from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketListSerializer
from .models import BucketList
# Create your views here.

class CreateView(generics.ListCreateAPIView):
    #This class defines the create behavior of our rest api
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer

    def perform_create(self, serializer):
        #save the post data when creating a new bucketlist
        serializer.save()
    '''Lets put a nice PUT and DELETE method handlers, which is all about http responses'''

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    #This class handles the HTTP GET, PUT and DELETE requests. 
    #RetrieveUpdateDestroyAPIView is a generic view that provides GET(one), PUT, PATCH and DELETE method handlers
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer