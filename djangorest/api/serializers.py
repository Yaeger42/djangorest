from rest_framework import serializers
from .models import BucketList

class BucketListSerializer(serializers.ModelSerializer):
    #Serializer to map the model instance into JSON format -- things start to get really interesting here
    #A class inside of a class... this is new
    class Meta:
        #MEta class to map serializers fields with the model fields
        model = BucketList
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created','date_modified')