from django.db import models

# Create your models here.

class BucketList(models.Model):
    #This class represents the bucketlist model.
    name = models.CharField(max_length = 255, blank = False, unique = True)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    #We use models.DateTimeField and auto_now_add to add the dates automatically

    def __str__(self):
        #Return a human readable representation of the model instance
        return "{}".format(self.name)